import os
from langchain_openai import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

class RAG:
    def __init__(self):

        self.chat = ChatOpenAI(
            # model="gpt-4o",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
            # base_url="...",
            # organization="...",
            # other params...
        )
        

        self.messages = [
            SystemMessage(content="You are a helpful assistant. that generates a good prompt for the given context and \
                        if you do not have context you replay with I do not have context."),
            HumanMessage(content="Hi AI, how are you today?"),
            AIMessage(content="I'm great thank you. How can I help you?"),
        ]

    def generate_answer(self, augmented_query: str):

        self.messages.append(HumanMessage(content=augmented_query))
        response = self.chat(self.messages)
        self.messages.append(response)
        return response.content
    