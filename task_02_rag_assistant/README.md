# Task 02: Document Q&A Assistant with RAG & Vector Embeddings

## Project Overview

This project is a Document Question-Answering Assistant built using Retrieval-Augmented Generation (RAG).

It allows users to retrieve relevant information from documents and generate answers based on the provided content.

The system uses local AI models and vector embeddings to provide context-based answers without requiring a paid LLM API.

## Features

- Load documents in TXT and PDF formats.
- Extract text and preserve document source metadata.
- Split documents into smaller chunks using Recursive Character Text Splitter.
- Generate vector embeddings using Sentence Transformers.
- Store document embeddings in ChromaDB.
- Retrieve relevant information using semantic similarity search.
- Generate answers using a locally running Llama 3.2 1B model through Ollama.
- Display source filenames and PDF page references with answers.

## Technologies Used

- Python 3.13
- LangChain
- Ollama
- Llama 3.2 1B
- Sentence Transformers
- ChromaDB
- PyPDF
- Hugging Face

## Project Structure

```text
task_02_rag_assistant/
│
├── data/
│   └── sample.txt
│
├── src/
│   ├── main.py
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   └── rag_pipeline.py
│
└── README.md
```

Note: The ChromaDB database is generated locally when the application runs and is excluded from GitHub.

## How It Works

1. **Document Loading:** Reads text and PDF documents.
2. **Text Splitting:** Divides documents into smaller chunks while preserving metadata.
3. **Embedding Generation:** Converts text chunks into numerical vector representations using `sentence-transformers/all-MiniLM-L6-v2`.
4. **Vector Storage:** Stores embeddings and document metadata in ChromaDB.
5. **Information Retrieval:** Finds relevant document chunks using similarity search.
6. **Answer Generation:** Uses the retrieved context to generate answers with the local Llama 3.2 1B model.
7. **Source Attribution:** Displays the source filename and page number when available.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shazmeen45/Datheon-AI-Internship.git
```

### 2. Navigate to the Project Directory

```bash
cd Datheon-AI-Internship
```

### 3. Create and Activate Virtual Environment

```bash
py -3.13 -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Install and Run Ollama

Download Ollama from:

https://ollama.com/download

Pull the required model:

```bash
ollama pull llama3.2:1b
```

Make sure Ollama is running before executing the application.

## Run the Project

From the repository root directory, execute:

```bash
python task_02_rag_assistant/src/rag_pipeline.py
```

The application will load the sample document, create embeddings, store them in ChromaDB, retrieve relevant information, and generate an AI answer.

## Example Question

**Question:**

What is Deep Learning and how does it relate to Machine Learning?

**Expected Answer:**

Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers to learn complex patterns from large amounts of data.

**Source:**

sample.txt

## Learning Outcomes

Through this project, I gained practical experience with:

- Retrieval-Augmented Generation (RAG).
- Document loading and text preprocessing.
- Text chunking and metadata preservation.
- Semantic search and vector embeddings.
- ChromaDB vector database.
- LangChain integration.
- Running local LLMs using Ollama.
- Building a document-based question-answering pipeline.

## Author

**Shazmeen Irshad**

GitHub: https://github.com/Shazmeen45

---

**Internship:**
