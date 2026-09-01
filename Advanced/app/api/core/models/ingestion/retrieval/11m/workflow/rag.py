from app.retrieval.retriever import retrieve_context
from app.llm.gemini import generate_answer


def ask_rag(question: str) -> dict:
    context = retrieve_context(question)

    answer = generate_answer(
        question=question,
        context=context,
    )

    return {
        "answer": answer,
        "sources": [],
    }