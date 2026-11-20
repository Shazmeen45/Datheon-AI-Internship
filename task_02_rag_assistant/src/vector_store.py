
from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


def create_vector_store(chunks):
    """
    Convert document chunks into embeddings
    and store text plus metadata in ChromaDB.
    """

    db_path = Path(__file__).resolve().parents[1] / "chroma_db"

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Delete the old collection if it exists
    if db_path.exists():

        old_store = Chroma(
            collection_name="langchain",
            embedding_function=embeddings,
            persist_directory=str(db_path)
        )

        old_store.delete_collection()

    # Store complete Document objects with metadata
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="langchain",
        persist_directory=str(db_path)
    )

    print("Vector database created successfully!")
    print("Total documents stored:", len(chunks))

    return vector_store


if __name__ == "__main__":

    from document_loader import load_document
    from text_splitter import split_text

    data_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "sample.txt"
    )

    documents = load_document(data_path)
    chunks = split_text(documents)

    vector_store = create_vector_store(chunks)

    # Test metadata retrieval
    results = vector_store.similarity_search(
        "What is Machine Learning?",
        k=2
    )

    print("\n========== RETRIEVED SOURCES ==========")

    for result in results:
        print("Source:", result.metadata.get("source"))

        if "page" in result.metadata:
            print("Page:", result.metadata["page"] + 1)

        print("Content:", result.page_content[:150])
        print("--------------------------------------")
