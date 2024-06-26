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

def get_test_prompts(num, Context, Objective):

    return f"""Understand the given context and generate {num} best test prompts based on the user's objective.

    Context:
    {Context}

    Objective:
    {Objective}

    ---

    Below is Instructions for LLM

    Based on the provided context and user's objective, generate a series of test prompts that could help in achieving the user's goal. The prompts should cover different aspects and scenarios to ensure comprehensive understanding and results. Here are some examples to guide you:

    1. **Summarization:**
    - Summarize the main points of the context related to the Objective.
    - Provide a brief summary focusing on specific aspect within the context.

    2. **Extraction:**
    - Extract key information about specific topic from the context.
    - List important facts or data points related to Objective.

    3. **Explanation:**
    - Explain how specific element in the context relates to Objective.
    - Describe the significance of particular detail in achieving Objective.

    4. **Clarification:**
    - Clarify the meaning of specific term or phrase mentioned in the context.
    - Provide additional details or background information about specific topic.

    5. **Question Generation:**
    - Generate questions that could help explore Objective further based on the context.
    - Create open-ended questions to facilitate deeper understanding of Objective.

    6. **Application:**
    - Suggest practical applications or implications of Objective based on the context.
    - Propose potential use cases or scenarios where Objective can be applied.

    OUTPUT FORMAT:
    Must be only one question perline
    Must be only questions, no extra text or other information

    """
