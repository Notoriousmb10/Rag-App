import fitz
from embeddingsMaker import embed_chunks_and_store


def pdfExtractor(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error Occurred: {e}")
        return None
    return text


text = pdfExtractor("harryPotter1.pdf")


def chunK_text(text, chunk_size=1000, overlap=200):
    start = 0
    chunksArray = []

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunksArray.append(text[start:end])
        start += chunk_size - overlap

    return chunksArray


chunks = chunK_text(text)
for i in range(len(chunks)):
    embed_chunks_and_store(chunks[i], i)
