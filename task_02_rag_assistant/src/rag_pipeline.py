
from pathlib import Path

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from document_loader import load_document
from text_splitter import split_text
from vector_store import create_vector_store


def build_rag_pipeline(document_name="sample.txt"):

    data_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / document_name
    )

    # 1. Load document
    print("\nLoading document...")
    documents = load_document(data_path)

    # 2. Split document
    print("Splitting document...")
    chunks = split_text(documents)

    print(f"Total chunks created: {len(chunks)}")

    # 3. Create vector database
    print("Creating vector database...")
    vector_store = create_vector_store(chunks)

    # 4. Initialize local LLM
    print("Initializing local LLM...")

    llm = ChatOllama(
        model="llama3.2:1b",
        temperature=0,
        num_predict=200
    )

    # 5. Create RAG prompt
    prompt = ChatPromptTemplate.from_template(
        """
You are a document question-answering assistant.

Answer the question using ONLY the provided context.

CONTEXT:
{context}

QUESTION:
{question}

INSTRUCTIONS:
- Answer only the exact question asked.
- Use the retrieved context to answer.
- Focus on the main concept in the question.
- Explain relationships between concepts when asked.
- Use 2 to 4 simple sentences.
- Do not include unrelated definitions.
- Do not invent information.
- If the required information is missing from the context,
  clearly say that the document does not provide it.

ANSWER:
"""
    )

    print("RAG pipeline created successfully!")

    return vector_store, llm, prompt


def ask_question(vector_store, llm, prompt, question):

    # 1. Retrieve relevant chunks
    print("\nSearching documents...")

    documents = vector_store.similarity_search(
        question,
        k=5
    )

    if not documents:
        print("No relevant information found.")
        return

    # 2. Prepare context
    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # 3. Display retrieved context
    print("\n========== RETRIEVED CONTEXT ==========")
    print(context)
    print("=======================================")

    # 4. Generate answer
    messages = prompt.format_messages(
        context=context,
        question=question
    )

    print("\nGenerating AI answer...")

    response = llm.invoke(messages)

    # 5. Display answer
    print("\n========== QUESTION ==========")
    print(question)

    print("\n========== AI ANSWER ==========")
    print(response.content)

    # 6. Display source citations
    print("\n========== SOURCES ==========")

    displayed_sources = set()

    for document in documents:

        source = document.metadata.get(
            "source",
            "Unknown source"
        )

        page = document.metadata.get("page")

        if page is not None:
            citation = f"{source}, Page {page + 1}"
        else:
            citation = source

        if citation not in displayed_sources:
            print(f"- {citation}")
            displayed_sources.add(citation)

    print("==============================")


if __name__ == "__main__":

    vector_store, llm, prompt = build_rag_pipeline(
        "sample.txt"
    )

    user_question = input("\nEnter your question: ")

    ask_question(
        vector_store,
        llm,
        prompt,
        user_question
    )
