# Importing Packages
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

# ALTERNATIVE FOR FIRESTORE IS POCKET BASE(FREE)

# Steps For Making the Firebase-Firestore Database & then installing the Goolge Cloud CLI
# Which helps us to access the firestore database from our system.

"""
Steps to replicate this example:
1. Create a Firebase account
2. Create a new Firebase project and FireStore Database
3. Retrieve the Project ID
4. Install the Google Cloud CLI on your computer
    - https://cloud.google.com/sdk/docs/install
    - Authenticate the Google Cloud CLI with your Google account
        - https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev
    - Set your default project to the new Firebase project you created
5. pip install langchain-google-firestore
6. Enable the Firestore API in the Google Cloud Console:
    - https://console.cloud.google.com/apis/enableflow?apiid=firestore.googleapis.com&project=crewai-automation
"""

# Loading the Gemini or any other LLM API_KEY
load_dotenv()

# Setup For Firestore Database
PROJECT_ID = 'langchainlearning-f3bd1' # Firebase Project ID, Get it from Firebase Console
SESSION_ID = 'user_session_id' # It will be a proper session id for each user. 
# Session ID is the ID for each document in firestore
COLLECTION_NAME = 'chatHistory'

print('Initializing the Firestore Client')
firestoreClient = firestore.Client(project=PROJECT_ID)

print('Initialing the Firestore Collection - chatHistory')
chatHistory = FirestoreChatMessageHistory(
    client=firestoreClient,
    session_id=SESSION_ID,
    collection=COLLECTION_NAME
)

print('chatHistory Initialized.')
print('chatHistory From Firestore is: ',chatHistory.messages)

# Adding the System Message in chatHistory - Firestore Collection
chatHistory.add_message(SystemMessage(content='You are an expert Mobile App Developer Using Flutter. Response to user accuralty & precisely with out any font format.'))

# Initialzing the Gemini Model
print('Initialzing the Gemini Model')
geminiModel = ChatGoogleGenerativeAI(model='gemini-1.5-flash')



print('Start chatting with AI. Type exit for to Quit')

while True:

    # Takingg user input
    userInput = input('You: ')

    #Exiting If input == exit
    if userInput.lower() == 'exit':
        break
  
    #Adding the User Message In ChatHistory Of Firestore Database
    chatHistory.add_user_message(userInput)

    # Calling the GeminiModel by sending the chathistory messages
    aiResponse = geminiModel.invoke(chatHistory.messages)

    # Showing the AI Response to user
    print('AI: ',aiResponse.content)

    # Storing the AI Response in chatHistory Of Firestore Database
    chatHistory.add_ai_message(aiResponse.content)





print('Exit Done, Re-Run the project for restarting!')

