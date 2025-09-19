import chromadb
import uuid
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
client = chromadb.PersistentClient(path="./chroma_db") 
collection = client.create_collection('harry_potter')
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def embed_chunks_and_store(chunk, idx):
    try:
        embedding = model.encode(chunk).tolist()
        collection.add(
            ids=[f"chunk-{idx}-{uuid.uuid4().hex[:6]}"],
            documents=[chunk],
            embeddings=[embedding]
        )
        print(f"Stored chunk-{idx}")

    except Exception as e:
        print(f"Error processing chunk-{idx}: {e}")