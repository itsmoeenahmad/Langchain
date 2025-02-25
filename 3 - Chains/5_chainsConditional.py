# Importing Packages
from langchain.schema.output_parser import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableBranch
from dotenv import load_dotenv

# Importing API_KEY
load_dotenv()

# Loading the Gemini LLM
geminiAI = ChatGoogleGenerativeAI(
      model='gemini-1.5-flash'
)

# Defining the Prompts

flutterPromptTempalte = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template('You are an expert in flutter development'),
        HumanMessagePromptTemplate.from_template('{humanMessage}')
    ]
)

reactPromptTempalte = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template('You are an expert in react development'),
        HumanMessagePromptTemplate.from_template('{humanMessage}')
    ]
)

# Defining Chains - Only one will be run based on user input
flutterChain = flutterPromptTempalte | geminiAI | StrOutputParser()
reactChain = reactPromptTempalte | geminiAI | StrOutputParser()

# Conditional Chain
conditionalChain = RunnableBranch(
    (lambda input: input['framework'].lower() == 'flutter', flutterChain),
    (lambda input: input['framework'].lower() == 'react', reactChain),
    RunnableLambda(lambda _: 'Sorry, This framework is not supported')
)

# Calling the Chain
response = conditionalChain.invoke({
    'framework':'react',
    'humanMessage':'what is react?'
})

# Showing Response
print('Response is: ',response)
