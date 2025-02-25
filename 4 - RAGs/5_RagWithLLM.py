# Importing Packages
import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

# Importing API_KEY
load_dotenv()

# Defining Paths
currentPath = os.path.dirname(os.path.abspath(__file__))
booksPath = os.path.join(currentPath, 'db', 'documents')
chromaPath = os.path.join(currentPath, 'db', 'chromaDB_MetaData')

# Embeddings
embeddings = OpenAIEmbeddings(
    model='text-embedding-3-small'
)

# Chroma DB
db = Chroma(
    persist_directory = chromaPath,
    embedding_function = embeddings
)

# User Query
userQuery = 'How is Moeen Ahmad?'

# Retriever
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={'k': 3}
)

# Gettingg userquery from the documents/books
booksResponse = retriever.invoke(userQuery)


#print('Response is: ',booksResponse)

# Showing the books response
#print('--------- Books Response Is: ---------')
#for i, doc in enumerate(booksResponse, 1):
#    print('Documents # ',i,' \n Data Is: ',doc.page_content)



# Definig the combined prompt
combinedPrompt =  (
    "Here are some documents that might help answer the question: "
    + userQuery
    + "\n\nRelevant Documents:\n"
    + "\n\n".join([doc.page_content for doc in booksResponse])
    + "\n\nPlease provide a rough answer based only on the provided documents. If the answer is not found in the documents, respond with 'I'm not sure'."
)

#print('RESPONSE IS:\n ',combinedPrompt)

# Open AI Model
openAI = ChatOpenAI(
    model='gpt-4o'
)

#Definiing Messages
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=combinedPrompt),
]

# Calling LLM
result = openAI.invoke(messages)

print(result)