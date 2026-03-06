from rag.loader import pdf_loader
from rag.chuncker import text_chunk
from rag.embeddings import generate_embeddings
from rag.vector_store import vector_store
from rag.loader import load_pdf, PDFExtractionError


def run_pipeline():
    file_path = "sample.pdf"

    try:
        text = load_pdf(file_path)

    except PDFExtractionError as e:
        print("\n⚠️ Document Processing Error")
        print("--------------------------------")
        print(str(e))
        print("\nSuggested fix:")
        print("• Try uploading a digital PDF with selectable text.")
        print("• If the document is scanned, run OCR first.")
        exit()

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
