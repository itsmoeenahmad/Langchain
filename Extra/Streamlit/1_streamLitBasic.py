# Importing Packages
import streamlit as streamlit
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Loading GEMINI API KEY
load_dotenv()


# Streamlit - Title
streamlit.title('Chat With LLM') 

# Streamlit - Subtitle
streamlit.text('~By Moeen Ahmad')


# Taking user input
userQuery = streamlit.text_input('Enter your Query')

# Button For Calling the LLM
buttonClicked = streamlit.button('Ask LLM')

llm = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash'
)

if buttonClicked:
    if userQuery is not None:
        with streamlit.spinner('Generating'):
            # Calling the LLM
            llmResponse = llm.invoke(userQuery)

            # Showing the LLM Response
            streamlit.write(llmResponse.content)
    else:
        streamlit.warning('Enter the text before clicking')    

    


