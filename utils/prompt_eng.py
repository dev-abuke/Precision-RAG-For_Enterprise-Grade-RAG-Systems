from langchain_pinecone import PineconeVectorStore


def augment_prompt(query: str, pinecone_vector_db: PineconeVectorStore):
    # get top 3 results from knowledge base
    results = pinecone_vector_db.similarity_search(query, k=3)
    # get the text from the results
    source_knowledge = "\n".join([x.page_content for x in results])
    # feed into an augmented prompt
    augmented_prompt = f"""Using the contexts below, answer the query.
    Contexts:
    {source_knowledge}
    Query: {query}"""
    return augmented_prompt