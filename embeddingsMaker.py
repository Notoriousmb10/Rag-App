import google.generativeai as genai

genai.configure(api_key="AIzaSyC7sroFqmgwJ7M0")


def embed_chunks(chunk):
    chunk_embeddings = []
        res = genai.embed_content(model="models/embedding-001", content=chunk)
        chunk_embeddings.append({"text": chunk, "embedding": res["embedding"]})
        
        
        
    
    
        

    
