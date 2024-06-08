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
    - Generate questions that could help explore Objective further .
    - Create open-ended questions to facilitate deeper understanding of Objective.

    6. **Application:**
    - Suggest practical applications or implications of Objective.
    - Propose potential use cases or scenarios where Objective can be applied.

    OUTPUT FORMAT:
    Must be list of questions only
    No extra text
    No numbering or other sequential decorations
    All questions must be on their own lines

    EXAMPLE OUTPUT:
    Summarize the main points related to Objective.
    Extract key information about specific topic.
    Explain how specific element relates to Objective.
    Clarify the meaning of specific term or phrase mentioned.
    Generate questions that could help explore Objective further.
    Suggest practical applications or implications of Objective .
    

    """