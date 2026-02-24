from rag.loader import load_documents
from rag.chuncker import chunk_text
from rag.embeddings import generate_embeddings
from rag.vector_store import vector_store


def run_pipeline():
    file_path = "grok_report (1).pdf"

    print("Loading documents...")
    documents = load_documents(file_path)

    print("Chunking text...")
    chunks = chunk_text(documents)

    print("Generating embeddings...")
    embeddings = generate_embeddings(chunks)

    print("Creating vector store...")
    index = vector_store(embeddings)


if __name__ == "__main__":
    run_pipeline()
