# Custom_RAG
Tech Support QA Assistant
# Tech Support QA Assistant

This project is an intelligent tech support question answering assistant built using LangChain and Ollama language models. It retrieves relevant context from a tech support dataset and then generates helpful, concise answers to customer queries along with average resolution times.

---

## Features

- Uses OpenAI-like Ollama LLM (`deepseek-r1`) to generate answers.
- Retrieves relevant context from a Chroma vector store built on a tech support dataset.
- Embeddings are created with the `mxbai-embed-large` model from Ollama.
- Supports continuous querying in a command line interface.
- Provides clear, context-driven answers mentioning average resolution times.

---

## Project Structure

- `main.py`: The main script that runs the chat loop. Retrieves context and generates answers.
- `vector_search.py`: Builds or loads the vector database from a CSV dataset and creates embeddings.
- `tech_support_dataset.csv`: Dataset containing tech support conversation logs, issues, responses, and resolution times.

---

## Installation

1. Clone this repository:

git clone <repo-url>
cd <repo-directory>

2. Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate


3. Install dependencies:

pip install -r requirements.txt


4. Make sure you have the `tech_support_dataset.csv` file in the project directory.

---

## Usage

Run the main.py script to start the chat assistant.

Then, enter your tech support-related questions when prompted. Type `stop` to exit.

Example:

How can I install this "xyz" software?

## Notes

- Ensure your Ollama models (`deepseek-r1` for LLM and `mxbai-embed-large` for embeddings) are installed and accessible.
- The vector store is created/persisted locally in the `./ChromaDB22` folder.
- Adjust the vector store retrieval `k` parameter to control how many documents to search.

## Author

Suyash Kulkarni
LinkdIn: https://www.linkedin.com/in/suyash-kulkarni-9094922b7/
