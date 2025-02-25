# Importing Packages
import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# Fetching the paths
currentPath = os.path.dirname(os.path.abspath(__file__))
chromaDBPath = os.path.join(currentPath, 'db', 'chromaDB')

# Defining the Embedding Model 
embeddings = OpenAIEmbeddings(
    model='text-embedding-3-small'
)

# Load the Exsiting Chroma DB
db = Chroma(
    persist_directory=chromaDBPath, 
    embedding_function=embeddings
)

# User Query Is
userQuery = 'How is Moeen Ahmad'

# Defining the Retriever which helps us to fetch the query related document from the db
retriever = db.as_retriever(
    search_type="similarity_score_threshold", # Type of search
    search_kwargs={"k": 2, "score_threshold": 0.1}, 
    # k = 2 means 'returns the 2 relevant doucments' 
    # 0.3 means 'retrieves documents which have at least 3% similarity'
)

# Lets retrieves the user query from the DB
relevantDocs = retriever.invoke(userQuery)

# Displaying the results
print('---------- Result is: ----------\n')
print(len(relevantDocs))
if len(relevantDocs)<1:
    print('---------- No Document Found Sorry ----------\n')
else:
    for i, doc in enumerate(relevantDocs, 1):
        print('Document # ',i,'\n','Data is: ',doc.page_content)

