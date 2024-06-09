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

        self.pc = Pinecone(api_key=pinecone_api_key)

        existing_indexes = [index_info["name"] for index_info in self.pc.list_indexes()]

        if self.index_name not in existing_indexes:
            self.pc.create_index(
                name=self.index_name,
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
            while not self.pc.describe_index(self.index_name).status["ready"]:
                time.sleep(1)

        self.index = self.pc.Index(self.index_name)

        return self.index, self.pc
    
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

    def query(self, query: str):
        """
        This function performs a query using the Pinecone index.
        
        Args:
            query (str): The query to search for.
        
        Returns:
            None. It prints the results of the query.
        """
        
        # Embed the query using the embeddings model.
        xq = self.embeddings.embed_query(query)
        
        # Perform a query on the Pinecone index.
        xc = self.index.query(vector=xq, top_k=5, include_metadata=True)
        
        # Initialize an empty list to store the results of the query.
        query_results = []
        
        # Iterate over the results of the query.
        for result in xc['matches']:
            
            # Retrieve the text from the result.
            # The text is stored in the 'text' field of the metadata.
            # The metadata is a dictionary and the text is split into lines.
            # We join the lines back into a single string.
            text = " ".join(result['metadata']['text'].split("\n"))
            
            # Create a dictionary to store the result of the query.
            # The score is rounded to 2 decimal places.
            result_dict = {
                "score": round(result['score'], 2),
                "text": text
            }
            
            # Add the result dictionary to the list of query results.
            query_results.append(result_dict)
            
            # Print the score and text of the result.
            # The f-string is used to format the string with the score and text.
            print(f"{result_dict['score']}: {text}")
