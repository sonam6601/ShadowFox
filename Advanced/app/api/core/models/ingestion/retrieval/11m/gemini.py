from google import genai

from app.core.config import settings


client = genai.Client(api_key=settings.google_api_key)


def generate_answer(question: str, context: str) -> str:
    prompt = f"""
You are a helpful RAG assistant.

Answer the user's question using the provided context.
If the answer is not available in the context, clearly say that
you don't have enough information.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model=settings.llm_model,
        contents=prompt,
    )

    return response.text or "I could not generate an answer."