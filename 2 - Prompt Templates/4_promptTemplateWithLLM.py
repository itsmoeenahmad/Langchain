# Importing Packages
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Loading the GEMINI API KEY
load_dotenv()

# Defining the Prompt Template

promptIs = PromptTemplate(
    input_variables=['topic','words'],
    template='Write down an essay on {topic}, which contain {words} words'
)

# METHOD # 01

# Final Prompt
#userPromptIs = promptIs.format_prompt(topic='Generative AI',words=100)

# METHOD # 02

# Let's take the inputs from user

userInputTopic = input('Enter the topic for essay: \n') 
userInputWords = input('Enter the words length for essay: \n')

# Final Prompt Is:
userPromptIs = promptIs.format(topic=userInputTopic,words=userInputWords)

# Defining the LLM - Gemini
geminiAI = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash'
)

# Calling the LLM
responseIs = geminiAI.invoke(userPromptIs)
print(responseIs.content)
