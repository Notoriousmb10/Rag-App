import google.generativeai as genai


genai.configure(api_key="AIzaSyCDkm2Z9Zvd8M")


def embed_chunks(chunks):
    embeddings = []
    for chunk in chunks:
        res = genai.embed_content(model="models/embedding-001cls", content=chunk)
        embeddings.append({"text": chunk, "embedding": res["embedding"]})

    return embeddings
