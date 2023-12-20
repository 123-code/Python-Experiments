import os 
from openai import OpenAI


from retry import retry 
import re 
from string import Template 
import json
from neo4j import GraphDatabase
import glob 
from timeit import default_timer as timer
from dotenv import load_dotenv
from time import sleep



project_prompt_template = """
From the Project Brief below, extract the following Entities & relationships described in the mentioned format 
0. ALWAYS FINISH THE OUTPUT. Never send partial responses
1. First, look for these Entity types in the text and generate as comma-separated format similar to entity type.
   `id` property of each entity must be alphanumeric and must be unique among the entities. You will be referring this property to define the relationship between entities. Do not create new entity types that aren't mentioned below. Document must be summarized and stored inside Project entity under `summary` property. You will have to generate as many entities as needed as per the types below:
    Entity Types:
    label:'Project',id:string,name:string;summary:string //Project mentioned in the brief; `id` property is the full name of the project, in lowercase, with no capital letters, special characters, spaces or hyphens; Contents of original document must be summarized inside 'summary' property
    label:'Technology',id:string,name:string //Technology Entity; `id` property is the name of the technology, in camel-case. Identify as many of the technologies used as possible
    label:'Client',id:string,name:string;industry:string //Client that the project was done for; `id` property is the name of the Client, in camel-case; 'industry' is the industry that the client operates in, as mentioned in the project brief.
    
2. Next generate each relationships as triples of head, relationship and tail. To refer the head and tail entity, use their respective `id` property. Relationship property should be mentioned within brackets as comma-separated. They should follow these relationship types below. You will have to generate as many relationships as needed as defined below:
    Relationship types:
    project|USES_TECH|technology 
    project|HAS_CLIENT|client


3. The output should look like :
{
    "entities": [{"label":"Project","id":string,"name":string,"summary":string}],
    "relationships": ["projectid|USES_TECH|technologyid"]
}

Case Sheet:
$ctext
"""


print("Hola Mundo")

load_dotenv()

#openai.api_type("azure")
'''
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
'''

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 
neo4j_url = os.getenv("NEO4J_URL")
neo4j_user = os.getenv("NEO4J_USER")
neo4j_pass = os.getenv("NEO4J_PASSWORD")
gds = GraphDatabase.driver(neo4j_url, auth=(neo4j_user, neo4j_pass))


def process_gpt(content,prompt):
    completion = client.chat.completions.create(
   
    temperature=0,
    max_tokens=150,

    model="gpt-3.5-turbo", 
    messages = [
        {"role":"system","content":prompt},
        {"role":"user","content":content}
    ])

    with open('gpt_response.txt', 'w') as f:

        f.write(completion.choices[0].message.content)
    nlp_results = completion.choices[0].message.content
    sleep(8)
    return nlp_results

def extract_entities(folder,prompt_template):
    files = glob.glob(f'data/{folder}/*')
    system_msg = "You are a helpful IT-project and account management expert who extracts information from documents."
    print(len(files))
    results = []

    for i, file in enumerate(files):
        try:
            with open(file,"r") as f:
                text = f.read().rstrip()
                prompt = Template(prompt_template).substitute(ctext=text)
                result = process_gpt(prompt,system_msg)
                results.append(json.loads(result))

        except Exception as e:
            print(f"Error processing {file}: {e}")
            print(e)

    return results
           
        
result = extract_entities("messages",project_prompt_template)

with open("test.json","w") as f:
    json.dump(result,f)



