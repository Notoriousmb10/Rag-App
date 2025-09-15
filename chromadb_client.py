import chromadb

client = chromadb.Client()
collection = client.create_collection("harry_potter")


def store_embeddings(embeddings):
    ids = [f"chunks-{i}" for i in range(len(embeddings))]
    texts = [e["text"] for e in embeddings]
    vectors = [e["embedding"] for e in embeddings]

    collection.add(ids=ids, texts=texts, embeddings=vectors)
