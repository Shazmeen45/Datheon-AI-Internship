
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

from document_loader import load_document


def split_text(documents, chunk_size=500, chunk_overlap=50):
    """
    Split documents into smaller chunks
    while preserving their source metadata.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":

    data_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "sample.txt"
    )

    print("Loading document...")

    documents = load_document(data_path)

    print("Splitting document...")

    chunks = split_text(documents)

    print("\nTotal chunks created:", len(chunks))

    for index, chunk in enumerate(chunks):

        print(f"\n========== CHUNK {index + 1} ==========")

        print("Source:", chunk.metadata.get("source"))

        if "page" in chunk.metadata:
            print("Page:", chunk.metadata["page"] + 1)

        print("Content:")
        print(chunk.page_content)
