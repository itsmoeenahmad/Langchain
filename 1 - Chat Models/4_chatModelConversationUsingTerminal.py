# Importing Packages We Need
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

# Loading API KEY
load_dotenv()

# Loading the GEMINI_API_KEY
gemini_LLM = ChatGoogleGenerativeAI(model='gemini-1.5-flash') 

# List Which store the messages
chatHistory = []

# System Message
systemMessage = SystemMessage(content='You are an expert in Flutter Mobile App Development, Response the user without any * or any format for making the font better. Response precise & accurate.')

# Storing the System Message in a ChatHistory List
chatHistory.append(systemMessage)

# Loop For Showing the You & AI Message In Terminal & Executing the LLM Request & showing response
while True:
    
    # Inputting user Query
    userInput = input('YOU: ')
    
    # Exiting If User Enter exit
    if userInput.lower() == 'exit':
        break

    # Storing the user message in Chat History List
    chatHistory.append(HumanMessage(content=userInput))

    # Executing Gemini Request Using ChatHistory & Storing again in ChatHistory
    geminiResponseIs = gemini_LLM.invoke(chatHistory)
    aiMessageIs = geminiResponseIs.content
    chatHistory.append(AIMessage(content=aiMessageIs))

    # Showing the AI Response:
    print('AI: ',aiMessageIs)

print('Thank You, Re-Run The File For Restarting')


    
