from langchain_community.llms import Ollama
from langchain.prompts.prompt import PromptTemplate
from langchain_community.chat_models import ChatOllama
import json

llm = ChatOllama(model="llama2",format="json",temperature=0.7)

prompt = PromptTemplate(
        template="""
        Eres un asistente util y amigable, capaz de escribir codigo de python, de alta calidad\n
        mismo que puede ser usado para realizar diversas tareas, como escribir a un archivo de excel, o realizar calculos matematicos\n
.""",
    input_variables=[]
    )

codigo = llm.invoke("Escribe codigo de python para multiplicar 2 números,el 5 y el 67")



print(codigo)
result = exec(codigo)
print(result)