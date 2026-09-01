from app.retrieval.vector_store import search_documents
from app.llm.generator import generate_answer


def ask_rag(question: str):
    try:
        documents = search_documents(question, k=5)

        if not documents:
            return {
                "answer": "I could not find relevant information in the uploaded documents.",
                "sources": []
            }

        context = "\n\n".join(documents)

        answer = generate_answer(question, context)

        return {
            "answer": answer,
            "sources": documents
        }

    except Exception as e:
        return {
            "answer": f"ERROR: {type(e).__name__}: {str(e)}",
            "sources": []
        }