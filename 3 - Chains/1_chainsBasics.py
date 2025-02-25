# Importing Pacakges
from langchain.schema.output_parser import StrOutputParser # Used for converting the LLM response to content Only
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Loading the API_KEY
load_dotenv()

# Defining the prompt
chatPromptIs = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(" You're an expert {frameWork} mobile app developer, Response to user accuratly & precisely. Don't use anythingg which effect the response."),
        HumanMessagePromptTemplate.from_template('{humanMessage}')
    ]
)

# Creating the Gemini LLM
geminiAI = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash'
)


# Defining the Chain

chainIs = chatPromptIs | geminiAI | StrOutputParser()

responseIs = chainIs.invoke({"frameWork":'flutter',"humanMessage":'Write down the meaning of reactnative'})

# Showing the Response
print('AI Response is: ',responseIs)
