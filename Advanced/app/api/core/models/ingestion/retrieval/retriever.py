from app.retrieval.vector_store import search_documents


def retrieve_context(query: str, top_k: int = 5) -> str:
    documents = search_documents(query, top_k=top_k)

    if not documents:
        return ""

    return "\n\n---\n\n".join(documents)