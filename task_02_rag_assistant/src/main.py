
from pathlib import Path

from rag_pipeline import build_rag_pipeline, ask_question


def main():

    print("===================================")
    print("   DOCUMENT Q&A ASSISTANT")
    print("===================================")

    # Show available documents
    data_folder = (
        Path(__file__).resolve().parents[1]
        / "data"
    )

    available_files = [
        file.name
        for file in data_folder.iterdir()
        if file.is_file()
        and file.suffix.lower() in [".txt", ".pdf"]
    ]

    if not available_files:
        print("No TXT or PDF documents found in data folder.")
        return

    print("\nAvailable documents:")

    for index, file_name in enumerate(available_files, start=1):
        print(f"{index}. {file_name}")

    # Ask user to select a document
    while True:

        try:
            choice = int(input("\nSelect document number: "))

            if 1 <= choice <= len(available_files):
                selected_file = available_files[choice - 1]
                break

            print("Invalid selection. Please try again.")

        except ValueError:
            print("Please enter a valid number.")

    print(f"\nSelected document: {selected_file}")

    # Build RAG pipeline
    vector_store, llm, prompt = build_rag_pipeline(
        selected_file
    )

    print("\nAsk questions about your document.")
    print("Type 'exit' to close the assistant.")

    # Chat loop
    while True:

        user_question = input("\nEnter your question: ")

        if user_question.lower().strip() == "exit":
            print("\nThank you for using Document Q&A Assistant!")
            break

        if not user_question.strip():
            print("Please enter a valid question.")
            continue

        ask_question(
            vector_store,
            llm,
            prompt,
            user_question
        )


if __name__ == "__main__":
    main()
