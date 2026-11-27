
# Task 03: Multi-Tool Autonomous AI Agent

## Project Overview

This project is a Multi-Tool Autonomous AI Agent built using Python, LangChain, and Ollama.

The agent uses a locally running Large Language Model (LLM) to understand user queries, select appropriate tools, execute tasks, and generate responses based on tool results.

It integrates three tools: Calculator, File Reader, and Web Search.

## Features

- **Calculator:** Performs mathematical calculations using Python.
- **File Reader:** Reads and retrieves information from a local text file.
- **Web Search:** Searches online information using DuckDuckGo.
- **Local LLM:** Uses Llama 3.2 1B through Ollama.
- **Tool Calling:** Uses LangChain to connect the AI model with multiple tools.
- **Source Links:** Includes retrieved web search results and source URLs in the final response.
- **Interactive CLI:** Allows users to interact with the agent through the terminal.

## Tools and Technologies

- Python 3.13
- LangChain
- LangChain Core
- LangChain Ollama
- Ollama
- Llama 3.2 1B
- DuckDuckGo Search (ddgs)

## Project Structure

```text
task_03_ai_agent/
│
├── data/
│   └── sample.txt
│
├── src/
│   ├── tools.py
│   ├── agent.py
│   └── main.py
│
└── README.md
```

## Available Tools

### 1. Calculator

Performs mathematical operations such as:

- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Exponentiation

Example:

```text
Calculate 250 * 4 using the calculator tool.
```

### 2. File Reader

Reads information from the `sample.txt` file and provides answers based on its content.

Example:

```text
According to sample.txt, explain what Deep Learning is.
```

### 3. Web Search

Uses DuckDuckGo to retrieve online search results, including titles, descriptions, and source URLs.

Example:

```text
Search the web for the latest developments in Artificial Intelligence and provide three results with source links.
```

## How It Works

1. The user enters a query through the terminal.
2. The AI agent analyzes the user's request.
3. LangChain connects the agent with the available tools.
4. The agent selects the appropriate tool.
5. The selected tool executes the requested task.
6. The tool returns its result to the agent.
7. The LLM generates a final response.
8. For web searches, the retrieved source information and URLs are included in the final output.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Shazmeen45/Datheon-AI-Internship.git
```

### 2. Navigate to the Project Directory

```bash
cd Datheon-AI-Internship
```

### 3. Create a Virtual Environment

```bash
py -3.13 -m venv .venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Install Ollama

Download and install Ollama:

https://ollama.com/download

### 7. Download the LLM Model

```bash
ollama pull llama3.2:1b
```

### 8. Run the AI Agent

From the repository root directory:

```bash
python task_03_ai_agent/src/main.py
```

## Example Interaction

**User:**

```text
Calculate 250 * 4 using the calculator tool.
```

**AI Agent:**

```text
The result of 250 * 4 is 1000.
```

## Testing

The following functionalities were tested successfully:

- Calculator tool execution.
- File Reader tool execution.
- Web Search tool execution.
- Retrieval of web search source URLs.
- AI-generated responses based on tool results.
- Interactive terminal exit command.

## Learning Outcomes

Through this project, I learned:

- Fundamentals of AI agents and autonomous tool selection.
- Integration of LangChain with a local LLM.
- Building custom Python tools.
- Implementing tool calling.
- Integrating web search functionality.
- Connecting multiple tools with an AI assistant.
- Working with Ollama and locally hosted language models.

## Cost and API Requirements

This project uses a locally hosted LLM through Ollama and free Python libraries.

No paid LLM API key or subscription is required.

## Author

Shazmeen Irshad

GitHub: https://github.com/Shazmeen45
