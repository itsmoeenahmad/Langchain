from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 
from dotenv import load_dotenv 

load_dotenv() # Loading the OPEN_API_KEY

# Store the messages, We will also store the new message which is basically the AIMessage
# Once, AI generate the message, store it manually & then also send it to the user
# It will be acting like a chatHistory
messages = [
    SystemMessage('You are an Expert Mobile App Developer'),
    HumanMessage('Give a tip related to mobile app development'),
]

# Defining the OPEN AI - LLM with Model
open_AI_LLM = ChatOpenAI(model='gpt-4o')

# Calling the OPEN_AI API & Passing the messages
responseIs = open_AI_LLM.invoke(messages)

print("OPEN_AI Response Is: ",responseIs.content)
