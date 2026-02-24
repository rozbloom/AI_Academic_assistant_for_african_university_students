def text_chunk(text: str, chunk_size=500, overlap=50):

    words = text.split()
    chunks = []
    start = 0
