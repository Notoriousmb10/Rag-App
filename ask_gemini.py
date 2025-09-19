from gemini import retrieve_content
import google.generativeai as genai


def question_gemini(question):
    content_chunks = retrieve_content(question)
    context_text = "\n\n".join(content_chunks)
    
    prompt = f"""
    You are a helpful assistant. Use only the following context to answer the question. If the answer is not in the context, say I don't know from the provided context."
    Context = {context_text}
    Question = {question}
    Answer:
    """
    
    response = genai.GenerativeModel('gemini-1.5-flash').generate_content(prompt)
    return response.text


ans = question_gemini('WWho reached the Triwizard Cup with Harry?')
print(ans)
