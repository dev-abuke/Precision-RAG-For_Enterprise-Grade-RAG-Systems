import time
import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

class PineconeVector:
    def __init__(self, index_name):
        self.index_name = index_name
        self.embeddings = OpenAIEmbeddings()
    def create_pinecone_index(self):
        pinecone_api_key = os.environ.get("PINECONE_API_KEY")

        pc = Pinecone(api_key=pinecone_api_key)

        existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

        if self.index_name not in existing_indexes:
            pc.create_index(
                name=self.index_name,
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
            while not pc.describe_index(self.index_name).status["ready"]:
                time.sleep(1)

        index = pc.Index(self.index_name)

        return index, pc
    
    def insert(self, split_documents):
        self.pinecone_vectorstore = PineconeVectorStore.from_documents(
            split_documents, 
            self.embeddings, 
            index_name=self.index_name
        )

        return self.pinecone_vectorstore
        
    def search_vectorstore(self, query: str):
        
        # get top 3 results from knowledge base
        results = self.pinecone_vectorstore.similarity_search(query, k=3)
        # check if there are any results
        if not results:
            raise ValueError("No results found in the knowledge base")
        # get the text from the results
        source_knowledge = "\n".join([x.page_content for x in results])

        return source_knowledge