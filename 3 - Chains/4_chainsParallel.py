# Importing Packages
from langchain.schema.runnable import RunnableParallel, RunnableLambda
from langchain.schema.output_parser import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from dotenv import load_dotenv

# Accessing the API_KEY
load_dotenv()

# Defining the Gemini LLM 
geminiLLM = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash'
)

# Prompt Templates:
flutterPromptTemplate = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template('You are an expert in flutter development.'),
        HumanMessagePromptTemplate.from_template('{humanMessage}')
    ]
)

reactPromptTemplate = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template('You are an expert in React development.'),
        HumanMessagePromptTemplate.from_template('{humanMessage}')
    ]
)

# Defining the Chains/Runnables - Which will be running in parallel
flutter = flutterPromptTemplate | geminiLLM | StrOutputParser()
react = reactPromptTemplate | geminiLLM | StrOutputParser()


# Creating The Parallel Chain
chain = RunnableParallel({
    'flutter': flutter,
    'react': react
})

# Calling/Starting the chain
response = chain.invoke({'humanMessage':'what is this framework?'})

# Showing the response
print('Flutter: ',response['flutter'])
print('React: ',response['react'])
