# Importing Packages
import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


# Defining Paths
currentPath = os.path.dirname(os.path.abspath(__file__))
chromaPath = os.path.join(currentPath, 'db','chromaDB_MetaData')

# Defininig Emdedding
embedding = OpenAIEmbeddings(
    model='text-embedding-3-small'
)

# Chroma DB
chromaDB = Chroma(
embedding_function=embedding,
persist_directory=chromaPath
)

# User Query
userQuery = "Who is Moeen?"

# Retriever
retriever = chromaDB.as_retriever(
    search_type='similarity_score_threshold',
    search_kwargs={"k": 1, "score_threshold": 0.1},
)

# Executing User Query Using Retriever
responseIs = retriever.invoke(userQuery)

print('Response is:',responseIs)

# Displaying the fetched Data
if len(responseIs)<1:
    print('Data Not Found')
else:
    for i, doc in enumerate(responseIs, 1):
        print('Document # ',i,'\n ',doc.page_content)
        print('Source: ',doc.metadata['source'])
