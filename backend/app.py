from flask import Flask, render_template, request, jsonify, make_response
import os, sys
from openai import OpenAI
from utility.env_manager import get_env_manager
from utility.pinecone import PineconeVector
from utility.pdf_ingestion import split_documents
from evaluation._data_generation import get_completion
from evaluation._data_generation import file_reader
from evaluation._evaluation import evaluate
from prompts.prompts import get_test_prompts
from utility.rag import RAG
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

sys.path.append("./uploaded_docs/")

PINECONE_INDEX_NAME = "pdf-doc"
pcv = PineconeVector(PINECONE_INDEX_NAME)
rag = RAG()

env_manager = get_env_manager()
zx = OpenAI(api_key=env_manager['openai_keys']['OPENAI_API_KEY'])

split_document = split_documents(doc_path="./uploaded_docs/10 Academy Cohort B - Weekly Challenge_ Week - 7.pdf")

index, pc = pcv.create_pinecone_index() 

vector = pcv.insert(split_document)

app = Flask(__name__)

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    return response

@app.before_request
def before_request():
    if request.method == 'OPTIONS':
        response = make_response()
        response = add_cors_headers(response)
        return response

@app.after_request
def after_request(response):
    response = add_cors_headers(response)
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    question = data.get('question')

    context_message = pcv.search_vectorstore(str(question))

    test_prompt_generator = get_test_prompts(num=5, Context=context_message, Objective=question)

    array_of_test_prompts = rag.generate_answer(test_prompt_generator)

    # context_message = file_reader("prompts/context.txt") # TODO add context with a given pdf
    prompt_message = file_reader("prompts/generic-evaluation-prompt.txt")

    context = str(context_message)
    prompt = str(prompt_message)
    
    prompt_score = []
    
    for test_prompt in array_of_test_prompts.splitlines():
        print("The Prompt is :: ", test_prompt)

        user_message = str(test_prompt)
    
        classification, accuracy = evaluate(prompt, user_message, context)

        print(classification, accuracy)

        # add to a dictionary
        prompt_score.append({'prompt': test_prompt, 'classification': classification, 'accuracy': accuracy})


    response = jsonify({'message': prompt_score, "status": True})
    response = add_cors_headers(response)
    # return 200 response and the classification and accuracy
    return response

if __name__ == '__main__':
    app.run(debug=True)
