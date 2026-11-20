# Task 02: Document Q&A Assistant with RAG & Vector Embeddings

## Project Overview

This project is a Document Question-Answering Assistant built using Retrieval-Augmented Generation (RAG).

It allows users to upload and select TXT or PDF documents, retrieve relevant information, and generate context-based answers using a locally running Large Language Model (LLM).

The application uses LangChain, Sentence Transformers, ChromaDB, and Ollama to provide document-based question answering without requiring a paid LLM API.

## Features

- Supports TXT and PDF document formats.
- Automatically detects available documents in the data folder.
- Allows users to select a document before asking questions.
- Extracts text while preserving source metadata.
- Splits documents into smaller chunks using Recursive Character Text Splitter.
- Generates vector embeddings using Sentence Transformers.
- Stores embeddings and document metadata in ChromaDB.
- Retrieves relevant information through semantic similarity search.
- Generates answers using the local Llama 3.2 1B model through Ollama.
- Displays source filenames and PDF page references with answers.
- Supports multiple questions in a single session.
- Uses a local LLM instead of a paid LLM API.

## Technologies Used

- Python 3.13
- LangChain
- Ollama
- Llama 3.2 1B
- Sentence Transformers
- Hugging Face
- ChromaDB
- PyPDF

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

**Note:** Users can add their own TXT or PDF documents inside the `data/` folder. The ChromaDB database is generated locally when the application runs and is excluded from GitHub.

## How It Works

1. **Document Loading:** Reads TXT and PDF documents using Python and PyPDF.
2. **Text Splitting:** Divides extracted text into smaller chunks using Recursive Character Text Splitter.
3. **Embedding Generation:** Converts text chunks into numerical vector representations using `sentence-transformers/all-MiniLM-L6-v2`.
4. **Vector Storage:** Stores document embeddings and metadata in ChromaDB.
5. **Information Retrieval:** Retrieves relevant document chunks using semantic similarity search.
6. **Answer Generation:** Uses retrieved context to generate answers with the locally running Llama 3.2 1B model.
7. **Source Attribution:** Displays the source filename and PDF page number when available.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shazmeen45/Datheon-AI-Internship.git
cd Datheon-AI-Internship
```

### 2. Create a Virtual Environment

```powershell
py -3.13 -m venv .venv
```

### 3. Activate the Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Install Ollama

Download and install Ollama:

https://ollama.com/download

Download the required model:

```bash
ollama pull llama3.2:1b
```

### 6. Run the Application

From the repository root directory, execute:

```bash
python task_02_rag_assistant/src/main.py
```

## How to Use

1. Place your TXT or PDF document inside `task_02_rag_assistant/data/`.
2. Run the application using the command above.
3. Select a document from the available documents list.
4. Enter a question related to the selected document.
5. The system retrieves relevant information and generates an answer.
6. Review the answer and its source references.
7. Type `exit` to close the assistant.

## Example Question

**Question:** What is Deep Learning?

**Expected Answer:** Deep Learning is a subset of Machine Learning that uses neural networks with multiple layers to learn complex patterns from large amounts of data.

**Source:** sample.txt

## Learning Outcomes

Through this project, I gained practical experience with:

- Retrieval-Augmented Generation (RAG)
- Document loading and text extraction
- Text preprocessing and chunking
- Vector embeddings
- Semantic similarity search
- ChromaDB vector storage
- LangChain integration
- Local LLM deployment using Ollama
- Document-based question answering
- Source metadata and page references

## Author

**Shazmeen Irshad**

GitHub: https://github.com/Shazmeen45

**Internship:** Python + Generative AI & LangChain Internship  
**Organization:** Datheon
