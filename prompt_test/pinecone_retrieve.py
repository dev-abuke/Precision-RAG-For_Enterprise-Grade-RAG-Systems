import os
import sys

# Add the directory containing 'utils' to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.pinecone import PineconeVector

def call_api(query, options, context):
    # Fetch relevant documents and join them into a string result.
    PINECONE_INDEX_NAME = os.environ.get("PINECONE_INDEX_NAME")

    pcv = PineconeVector(PINECONE_INDEX_NAME)

    query_result = pcv.query(query)

    # for doc in query_result:
    #     print(f"The score is {doc['score']} : {doc['text']}")

    text = query_result[0]["text"]

    # print(f"The text is {text}")

    result = {
        "output": text,
    }
    # Include error handling and token usage reporting as needed
    # if some_error_condition:
    #     result['error'] = "An error occurred during processing"
    #
    # if token_usage_calculated:
    #     result['tokenUsage'] = {"total": token_count, "prompt": prompt_token_count, "completion": completion_token_count}

    return result

# if __name__ == "__main__":
#     call_api("Who are the tutors for this weeks challenge?", {}, {})