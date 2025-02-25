# Importing Packages
import os # For Operating System - Which find out our current directory
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


# Paths
currentPath = os.path.dirname(os.path.abspath(__file__)) # Fetch our current file path
documentPath = os.path.join(currentPath, "documents","book.txt") # Fetch the book path using currentDirectory Path
chromaDBPath = os.path.join(currentPath, "db","chromaDB") # Path where our book data will be stored

# Condition For Checking that is the Chroma Vector DB Already exist or not
if not os.path.exists(chromaDBPath):
    print('------------- Chroma DB Path is not exist, Lets add it -------------')

    # Check that is the book/documents file exist or not
    if not os.path.exists(documentPath):
        raise FileNotFoundError(
            "The Document {documentPath} not exist. Please check the path & try again"
        )
    
    # Reading the content from the book/document
    textLoader = TextLoader(documentPath)
    dataIs = textLoader.load()

    #print('-------------------------------------------------------------------------')
    #print('------------- DATA IS -------------')
    #for doc in dataIs:
    #    print(doc)


    # Splitting the data into chunks
    textSplitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=50) 
    # chunkSize = 'Shows that how many characters will be there in each chunk'
    # chunkOverLap = '0 means that the in any chunk the previous chunk data will be not be available'
    documents = textSplitter.split_documents(dataIs)


    # Displaying the information about chunks:
    print('------------- Chunks data is -------------/n')
    print('Length of the chunks is: ',len(documents),'/n')
    print('First one Docuemnt/Chunk data is: ',documents[0].page_content)


    #Creatingg Embeddings
    print('------------- Lets create the embeddinggs -------------')
    embeddings = OpenAIEmbeddings(
        model='text-embedding-3-small'
    )
    
    #Chroma DB Code - For Saving the chunks
    print('------------- Lets save the embeddings with documents in Chroma DB -------------/n')
    db = Chroma.from_documents(
        documents, embeddings, persist_directory=chromaDBPath
    )
    print('------------- Finished Creating Embeddings -------------/n')




else:
    print('------------- Chroma DB Path already exist -------------')
