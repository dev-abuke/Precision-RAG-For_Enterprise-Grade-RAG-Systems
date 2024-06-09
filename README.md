# Precision RAG for Enterprise-Grade Systems

- [Overview](#overview)
- [Project Goals and Objectives](#project-goals-and-objectives)
  - [Automate Prompt Generation](#automate-prompt-generation)
  - [Implement Evaluation Data Generation](#implement-evaluation-data-generation)
  - [Develop a Robust Prompt Testing and Ranking System](#develop-a-robust-prompt-testing-and-ranking-system)
  - [Integrate Advanced Tools like Pinecone and LangChain](#integrate-advanced-tools-like-pinecone-and-langchain)
  - [Design a User-Friendly Interface](#design-a-user-friendly-interface)
  - [Ensure Comprehensive System Integration and Testing](#ensure-comprehensive-system-integration-and-testing)
- [Tech Stack](#tech-stack)
  - [Backend](#backend)
  - [Frontend](#frontend)
  - [Other Tools](#other-tools)
- [Project Structure](#project-structure)
- [Code Structure](#code-structure)
- [Installation](#installation)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Accessing the Backend Application](#accessing-the-backend-application)
- [Contributing](#contributing)
  - [How to Contribute](#how-to-contribute)
  - [Reporting Issues](#reporting-issues)
  - [Feature Requests](#feature-requests)
  - [License Information](#license-information)

## Overview

This project focuses on developing an enterprise-grade Retrieval-Augmented Generation (RAG) system that automates prompt generation, evaluation, and testing for Language Models (LLMs) like GPT-4. By integrating advanced prompt engineering techniques and cutting-edge tools like Pinecone and LangChain, this project aims to enhance the efficiency, effectiveness, and accessibility of LLMs in various business applications.

## Project Goals and Objectives

1. **Automate Prompt Generation**
   - Develop a system that can automatically generate high-quality prompts based on user inputs.

2. **Implement Evaluation Data Generation**
   - Create mechanisms to generate diverse test cases automatically for evaluating prompts.

3. **Develop a Robust Prompt Testing and Ranking System**
   - Use methodologies like Monte Carlo matchmaking and ELO rating systems to assess and rank the generated prompts.

4. **Integrate Advanced Tools like Pinecone and LangChain**
   - Utilize Pinecone for efficient vectorized data storage and retrieval and LangChain for seamless interaction with the RAG framework.

5. **Design a User-Friendly Interface**
   - Create an intuitive interface for users to input objectives, generate prompts, and view evaluation results.

6. **Ensure Comprehensive System Integration and Testing**
   - Integrate all components of the system and conduct thorough testing to ensure functionality, usability, and performance.

## Tech Stack

### Backend

- **Python**: The core programming language used for prompt generation, evaluation, and backend logic.
- **Flask**: A lightweight WSGI web application framework used to build the backend and serve the user interface.
- **Pinecone**: A vector database used for efficient storage and retrieval of vectorized data.
- **LangChain**: A framework to facilitate seamless interaction with the RAG system components.

### Frontend

- **HTML/CSS**: Standard technologies used for structuring and styling the web interface.
- **JavaScript**: Enhances interactivity and user experience on the frontend.
- **React**: A JavaScript library for building user interfaces, used to create a responsive and interactive frontend.

### Other Tools

- **Jupyter Notebooks**: Used for experimentation, development, and testing of various components and algorithms.
- **Git**: Version control system used for tracking changes and collaboration.
- **Virtual Environment**: Ensures a clean and isolated environment for dependency management.

## Project Structure

- `automatic_prompt_engineer/`: Contains the core code for the automatic prompt engineering system.
- `backend/`: Backend code for the project.
  - `evaluation/`: Code related to prompt evaluation.
  - `prompts/`: Code related to prompt generation.
  - `test-dataset/`: Dataset for testing the system.
  - `uploaded_docs/`: Directory for uploaded documents.
  - `utility/`: Utility scripts and functions.
  - `app.py`: Main backend application script.
- `data/`: Directory for storing data files.
- `DataRoom/`: Additional data resources.
- `frontend/`: Frontend code for the project.
- `notebooks/`: Jupyter notebooks for experimentation and development.
- `rag/`: RAG system implementation.
- `utils/`: Utility scripts.
  - `pdf_ingestion.py`: Script for ingesting PDF documents.
  - `pinecone.py`: Pinecone integration script.
  - `prompt_eng.py`: Prompt engineering script.
  - `rag.py`: RAG system script.
  - `req.py`: Script for handling requests.
- `promptfooconfig.yaml`: Configuration file.
- `requirements.txt`: List of dependencies required for the project.

## Code Structure

      ├── backend
      │   ├── main.py               # Main backend application script
      │   ├── routes                # API routes
      │   ├── evaluation            # Code related to prompt evaluation
      │   ├── prompts               # Code related to prompt generation
      │   ├── test-dataset          # Dataset for testing the system
      │   ├── uploaded_docs         # Directory for uploaded documents
      │   ├── utility               # Utility scripts and functions
      │   └── app.py                # Flask Entry point
      ├── data
      │   ├── any.pdf               # Raw data files
      │   └──
      ├── frontend
      │    └──src                   # source file directory
      │        ├──App.jsx           # Entry point main file
      │        └──ListPrompts.jsx   # used to populate List of prompts
      │
      ├── Dockerfile                # Docker configuration
      ├── docker-compose.yml        # Docker Compose configuration
      ├── requirements.txt          # List of dependencies required for the project
      ├── README.md                 # Project documentation
      ├── notebooks                 # Jupyter notebooks for experimentation and development
      ├── rag                       # RAG system implementation
      └── utils
         ├── pdf_ingestion.py      # Script for ingesting PDF documents
         ├── pinecone.py           # Pinecone integration script
         ├── prompt_eng.py         # Prompt engineering script
         ├── rag.py                # RAG system script
         └── req.py                # Script for handling requests


## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/dev-abbuke/precision-rag-for-enterprise-grade-systems.git
   ```
2. **Navigate to Directory**
   ```sh
   cd precision-rag-for-enterprise-grade-systems 
   ```
3. **Set Up Environment Variables**
   
   Create a .env file in the backend directory and add your environment variables, such as Pinecone API key and other configurations.

   ```sh
   touch .env
   ```
   Then add the fo;;owing and your API key

   ```sh
   OPENAI_API_KEY="sk-*****************************"
   PINECONE_API_KEY="******************************"
   ```
4. **Set Up Virtual Environment**

   ```sh
   python -m venv myenv
   source myenv/bin/activate   # On Windows use `env\Scripts\activate`
   ```

## Backend Setup
   1. **Navigate to the Backend Directory**
     
      ```sh
      cd backend
      ```
   2. **Run the Backend Application**

      ```sh
      flask --app app --debug run
      ```
   3. **Using Docker**

      #### If you prefer to run the application in a Docker container, follow these steps


      Build the Docker Image

      ```sh
      docker build -t backend-app .
      ```
      Run the Docker Container

      ```sh
      docker run -p 5000:5000 backend-app
      ```

## Frontend Setup
   1. **Navigate to the Frontend Directory**
     
      ```sh
      cd frontend
      ```

   2. **Install Frontend Dependencies**

       ```sh
      npm install
      ```

   3. **Run the Frontend Application**

      ```sh
      npm run dev
      ```
   4. **Using Docker**

      If you prefer to run the frontend application in a Docker container, follow these steps

      Build the Docker Image

      ```sh
      docker build -t frontend-app .
      ```

      Run the Docker Container:

      ```sh
      docker run -p 3000:3000 frontend-app
      ```

      Accessing the Application

      - Open your browser and go to http://localhost:5173 to access the frontend application.
      
## Accessing the Backend Application

   Open your browser and go to
   
   `http://localhost:5000` to access the backend application. 
   You can use tools like `Postman` `Thunderclient` or `Curl` to send `POST` requests to `http://localhost:5000/generate` with a JSON payload to generate prompts.

   Example JSON Payload for `/generate` Endpoint
   ```sh
   {
   "question": "What is the impact of AI on social media management?"
   }
   ```
   **API Endpoints**
   - `POST /generate` Generates prompts based on the input question and returns the evaluation scores.

## Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these guidelines.

## How to Contribute

1. **Fork the Repository**

   Start by forking the repository to your GitHub account. This will create a copy of the repository under your username.

2. **Clone the Repository**

   Clone the forked repository to your local machine:

   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

## Reporting Issues
If you encounter any issues or bugs, please open an issue on GitHub. Provide as much detail as possible to help us resolve the issue quickly.

## Feature Requests
We welcome new ideas and feature requests. If you have a suggestion for improving the project, please open an issue on GitHub and describe your idea.

## License Information

See https://github.com/dev-abuke/Precision-RAG-For_Enterprise-Grade-RAG-Systems/blob/main/License.md

## Thank you for contributing!






