from pypdf import PdfReader
import os


class PDFExtractionError(Exception):
    pass


def load_pdf(file_path: str):

    if not os.path.exists(file_path):
        raise PDFExtractionError(
            "The file could not be found. Please check the file path."
        )

    try:
        reader = PdfReader(file_path)
    except Exception:
        raise PDFExtractionError(
            "The PDF file appears corrupted or unsupported."
        )

    if reader.is_encrypted:
        raise PDFExtractionError(
            "This PDF is encrypted or password-protected. Please unlock it before uploading."
        )

    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    if len(text.strip()) == 0:
        raise PDFExtractionError(
            "No readable text was found in the PDF. This often happens when the document is a scanned image. Consider using OCR."
        )

    return text
