from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(doc_path: str = "./data/10 Academy Cohort B - Weekly Challenge_ Week - 7.pdf"):
    try:
        # load raw docs from all files in the directory
        directory_loader = PyPDFLoader(doc_path)

        # load raw docs from all files in the directory in parallel
        raw_docs = directory_loader.load()

        # Split text into chunks in parallel
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        
        # Split text into chunks in parallel and store the embeddings in the vector store
        docs = text_splitter.split_documents(raw_docs)
        
        return docs

    except Exception as error:
        print('error', error)
        raise Exception('Failed to split your data')