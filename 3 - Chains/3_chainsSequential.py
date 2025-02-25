# Importing Packages
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema.runnable import RunnableLambda
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv

# Here I'm just showing you how sequential chains work: So I call the LLM & then the response from the LLM
# I'm showingg it to user in full lower case.

# Loading API_KEY
load_dotenv()

# Defining Chat Prompt
chatPromptTemplate = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template('You are an AI helper'),
        HumanMessagePromptTemplate.from_template('{humanMessage}')
    ]
)

# Defining the Gemini LLM Model
geminiLLM = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash'
) 

# Task For converting the LLM response to lower case
toLowerCase = RunnableLambda(lambda x: x.lower())

# Definig the Chain
chain = chatPromptTemplate | geminiLLM | StrOutputParser() | toLowerCase 

# Calling the Chain
outputIs = chain.invoke({'humanMessage':'generate me a motivational quote in upper case'})

print(outputIs)

