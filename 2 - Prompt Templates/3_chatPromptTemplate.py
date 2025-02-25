# Importing package
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

# Chat Prompt Template
chatPromptTemplate = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('Your an AI helper'),
    HumanMessagePromptTemplate.from_template('{humanMessage}')
])

#  Prompt Is
promptIs = chatPromptTemplate.format_messages(humanMessage='Generate me a best quote for motivivation')

# PromptIs return the list of messages. So, lets take a loop on it & print the content

for messageIs in promptIs:
    print(messageIs.content)
