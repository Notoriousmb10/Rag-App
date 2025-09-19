import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

if "harry_potter" in [c.name for c in client.list_collections()]:
    collection = client.get_collection("harry_potter")
else:
    print("Collection 'harry_potter' does not exist")
    exit()

# Fetch first 5 documents
docs = collection.get(limit=5, include=["embeddings", "documents"])
print(docs['embeddings'])