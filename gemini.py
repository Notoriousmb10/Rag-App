import os
from dotenv import load_dotenv
import google.generativeai as genai
from sentence_transformers import SentenceTransformer
import chromadb

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
client = chromadb.PersistentClient(path='./chroma_db')
collection = client.get_collection('harry_potter')


def retrieve_content(question, top_k=3):
    query_embedding = model.encode(question).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=['documents']
    )
    
    return results['documents'][0]