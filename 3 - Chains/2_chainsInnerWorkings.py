# Importing Packages
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Loading the API_KEY
load_dotenv()

# Defining the Gemini LLM Model
geminiAI = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash'
)

# Defining the Chat Prompt
chatPrompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("you are an expert in flutter development"),
        HumanMessagePromptTemplate.from_template("{humanMessage}")
    ]
)

# Creating the tasks, also known as Runnables
promptTemplate = RunnableLambda(lambda x: chatPrompt.format_prompt(**x)) # For extracting the messages converting.
llmModel = RunnableLambda(lambda x: geminiAI.invoke(x)) # Calling the LLM Model.
parseOutput = RunnableLambda(lambda x: x.content) # Getting the content from the LLM Response.

# Creating the Runnable Sequence
chain = RunnableSequence(first=promptTemplate, middle=[llmModel], last=parseOutput)

# Running the chain
llmResponse = chain.invoke({'humanMessage':'write down the note on text widget'})

# Showing Response
print('LLM RESPONSE IS: ',llmResponse)