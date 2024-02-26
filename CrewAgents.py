from langchain_community.llms import Ollama
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import AgentExecutor, create_self_ask_with_search_agent
from langchain.memory import ConversationBufferMemory


memory = ConversationBufferMemory()
tools = [DuckDuckGoSearchRun(max_results=1, name="Intermediate Answer")]
prompt = hub.pull("hwchase17/react")
llm = Ollama(model="mistral")
agent = create_self_ask_with_search_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

input_dict = {"input": "what is python", "tools": tools}
result = agent_executor.invoke(input_dict, return_intermediate_steps=True)