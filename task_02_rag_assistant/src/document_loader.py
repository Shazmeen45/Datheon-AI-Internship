
from pathlib import Path

from pypdf import PdfReader
from langchain_core.documents import Document


def load_document(file_path):
    """
    Load a TXT or PDF file and preserve source metadata.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    documents = []

    # Load TXT file
    if file_path.suffix.lower() == ".txt":

        text = file_path.read_text(
            encoding="utf-8"
        )

        if not text.strip():
            raise ValueError("The text file is empty.")

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": file_path.name
                }
            )
        )

    # Load PDF file
    elif file_path.suffix.lower() == ".pdf":

        reader = PdfReader(str(file_path))

        for page_number, page in enumerate(reader.pages):

            text = page.extract_text() or ""

            if text.strip():
                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "source": file_path.name,
                            "page": page_number
                        }
                    )
                )

        if not documents:
            raise ValueError(
                "No readable text found in the PDF."
            )

    else:
        raise ValueError(
            "Unsupported file format. Use TXT or PDF."
        )

    return documents


if __name__ == "__main__":

    data_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "sample.txt"
    )

    loaded_documents = load_document(data_path)

    print("Document loaded successfully!")
    print("Total document sections:", len(loaded_documents))

    print("\nSource information:")
    print(loaded_documents[0].metadata)

    print("\nDocument content:")
    print(loaded_documents[0].page_content)
