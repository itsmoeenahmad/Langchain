# Importing Packages
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain import hub # Provide us the prompts like React
from langchain.agents import create_react_agent, AgentExecutor, tool # Provide to create & execute agents.
import datetime # For Getting the system timing

# Loading API_KEY
load_dotenv()

# Method/Tool - Which will be call by agent at a time of taking action
@tool
def get_system_time():
    """ Returns the current date and time in the specified format """
    current_time = datetime.datetime.now()
    return current_time

# Definig the LLM - Open AI 
openAI = ChatOpenAI(
    model='gpt-4o'
)

# user Query
userQuery = 'What is the current time now?'

# Prompt Template - Of React Pattern
reactPromptTemplate = hub.pull('hwchase17/react')

# Defining the tools - One or many 
tools = [
    get_system_time
]

# Agent Is
agent =  create_react_agent(
    tools=tools,
    prompt=reactPromptTemplate,
    llm=openAI
)

# Agent Executor
agentExecutor = AgentExecutor(
    agent=agent,
    tools=tools,
    handle_parsing_errors=True,
    verbose=True # For Showing the Logs 
)

# Calling the agent
agentExecutor.invoke({'input': userQuery})