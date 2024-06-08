from langchain_pinecone import PineconeVectorStore


def augment_prompt(query: str, source_knowledge: str) -> str:
    # check if the query is None or empty
    if not query:
        raise ValueError("Query cannot be empty")
    # check if the pinecone_vector_db object is None
    if not source_knowledge:
        raise ValueError("Source knowledge object cannot be None")
    # feed into an augmented prompt
    augmented_prompt = f"""Using the contexts below, answer the query.
    Contexts:
    {source_knowledge}
    Query: {query}"""
    return augmented_prompt
