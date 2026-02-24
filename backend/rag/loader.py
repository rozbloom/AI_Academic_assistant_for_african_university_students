from pypdf import pdfreader


def pdf_loader(file_path: str) -> str:
    reader = pdfreader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text()
    return text
