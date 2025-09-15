import fitz

from embeddingsMaker import embed_chunks
from chromadb_client import store_embeddings


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
    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


chunks = chunK_text(text)
embeddings = embed_chunks(chunks)
save_to_chromaDB = store_embeddings(embeddings)
