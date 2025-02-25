# Importing Packages
import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# Paths
currentPath = os.path.dirname(os.path.abspath(__file__))
booksPath = os.path.join(currentPath, 'documents')
chromaPath = os.path.join(currentPath, 'db', 'chromaDB_MetaData')

# Condition For Checking that is the Chroma Vector DB Already exist or not
if not os.path.exists(chromaPath):
    print('------------- Chroma DB Path is not exist. Lets add it -------------')


    #Checking that if the books/files path exist or not
    if not os.path.exists(booksPath):
        raise FileNotFoundError("The Document {booksPath} not exist. Please check the path & try again")
    
    # List all text files in the directory
    booksLists = [f for f in os.listdir(booksPath) if f.endswith(".txt")]

    # Reading the text content from each file and store it with metadata
    documents = []
    print('----------------- Starting the loop -----------------')
    for bookIs in booksLists:
        eachBookPath = os.path.join(booksPath, bookIs)
        print('----------------- Each Book Path is: ',eachBookPath,'\n')
        loader = TextLoader(eachBookPath)
        loadedDataIs = loader.load() # It returns the list of documents/chunks
        #print('---------------- Loaded Data is: ',loadedDataIs,'\n')
        print('----------------- Another loop starting')
        for doc in loadedDataIs:
            print('----------------- Doc is: ',doc)
            doc.metadata = {'source':bookIs}
            documents.append(doc)
    
    
    # Splitting the data into chunks
    text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Defining the Embedding
    embeddings = OpenAIEmbeddings(
        model='text-embedding-3-small'
    )

    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=chromaPath
    )
    print('------------- Finished! -------------')
    


else:
    print('------------- Chroma DB Path is already exist. No need to add it again-------------')