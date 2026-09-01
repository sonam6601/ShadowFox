from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_answer(question: str, context: str):
    prompt = f"""
You are a helpful RAG assistant.

Answer the user's question using ONLY the information provided in the context.

If the answer is not present in the context, say:
"I could not find this information in the uploaded document."

Context:
{context}

Question:
{question}

Give a short and clear answer.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text