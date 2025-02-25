from langchain_openai import ChatOpenAI # Importing the ChatOpenAI Class From Langchain_openai
from dotenv import load_dotenv # Importing load_dotenv function for Accesing OPEN_API_KEY

load_dotenv() # For Loading the OPEN_API_KEY

openAI_LLM = ChatOpenAI(model='gpt-4o') # Defining the OpenAI Model, Which we will use.

responseIs = openAI_LLM.invoke('Write a one line quote') # Calling the OpenAI(LLM) with a prompt. (.invoke function help us to send a message to llm)

print('Response is: ',responseIs.content) # Showing the response of the openAI LLM