from rag.loader import pdf_loader
from rag.chuncker import text_chunk
from rag.embeddings import generate_embeddings
from rag.vector_store import vector_store


def run_pipeline():
    file_path = "sample.pdf"

    print("Loading documents...")
    documents = pdf_loader(file_path)

    print("TEXT LENGTH:", len(file_path))

    print("Chunking text...")
    chunks = text_chunk(documents)
    print("NUMBER OF CHUNKS:", len(chunks))

    print("Generating embeddings...")
    embeddings = generate_embeddings(chunks)

    print("Creating vector store...")
    index = vector_store(embeddings)


if __name__ == "__main__":
    run_pipeline()
