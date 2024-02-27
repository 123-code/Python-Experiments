from langchain import hub
from langchain_community.llms import Ollama
from langchain.tools import DuckDuckGoSearchRun,BaseTool, StructuredTool, tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.chat_models import ChatOllama
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_community.llms import Ollama
from langchain.prompts.prompt import PromptTemplate
from langchain.agents import initialize_agent
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import DuckDuckGoSearchRun,BaseTool, StructuredTool, tool
from langchain import hub
import openpyxl
import smtplib
from email.message import EmailMessage
import os
from sendgrid import SendGridAPIClient 
from sendgrid.helpers.mail import Mail
from langchain.agents import initialize_agent


llm = ChatOllama(model="llama2",format="json",temperature=0)
prompt = PromptTemplate(
        template="""You are a helpful assistant. able to perform various actions across excel spreadsheets \n 
        you are given a spreadsheet, and a possible scenario is that you have t read it, and retrieve its contents, use the tools available if you need to send emails.\n
        whenever you respond, you should do iyt in this format: \n
        ```json
{
    "action": "action_to_perform",
    "action_input": "file_name.xlsx"
}
```
.""",
    input_variables=[]
    )

conversational_memory = ConversationBufferWindowMemory(
        memory_key='chat_history',
        k=5,
        return_messages=True
)

class ExcelEmailSender(BaseTool):
    
    @property
    def is_single_input(self) -> bool:
        return True
    
    name = "Excel Email extractor"
    description = "use this tool when you need to get information about my appointments"
    
    def _run(self,inputs):
    
        workbook = openpyxl.load_workbook(os.path.join('.', 'data.xlsx'))
        sheet = workbook.active
        text_file = open('data.txt', 'w')
        
        for row in sheet.iter_rows():
            row_data = [] 
            for cell in row:
                if cell.value is not None:
                    row_data.append(str(cell.value))
                    
            text_file.write('\t'.join(row_data) + '\n')
            
        text_file.close()
        
        with open('data.txt', 'r') as f:
            file_contents = f.read()

        html_content = '<table border="1">'

        for row in file_contents.split('\n'):
            html_content += '<tr>'
            for cell in row.split('\t'):
                html_content += f'<td>{cell}</td>'
                html_content += '</tr>'
                html_content += '</table>'
                    
        message = Mail(
            from_email='jose.naranjo.martinez@udla.edu.ec',
            to_emails='naranjojose256@gmail.com',
            subject='Datos de tu hoja excel:',
            html_content=html_content)
        
        try:
            sg = SendGridAPIClient('')
            response = sg.send(message)     
            print(response.status_code)
            print(response.body)   
            print(response.headers)
        
        except Exception as e:
            print(e.message)

        """Use the tool."""
        return "LangChain"

  

    def _arun(self):
        
        raise NotImplementedError("This tool does not support async")
        return "Error"
    
tools = [ExcelEmailSender()]

# initialize agent with tools
agent = initialize_agent(
    agent='chat-conversational-react-description',
    tools=tools,
    llm=llm,
    verbose=True,
    prompt=prompt,
    max_iterations=3,
    early_stopping_method='generate',
    memory=conversational_memory
)

agent("Look at the Excel sheet named data.xlsx and tell me what are its contents.")