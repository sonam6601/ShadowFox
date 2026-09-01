import chromadb

from app.core.config import settings


client = chromadb.PersistentClient(
    path=settings.chroma_persist_dir
)

collection = client.get_or_create_collection(
    name="documents"
)


def add_documents(chunks: list[str]) -> None:
    if not chunks:
        return

    ids = [f"chunk_{i}" for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
    )


def search_documents(query: str, top_k: int = 5) -> list[str]:
    results = collection.query(
        query_texts=[query],
        n_results=top_k,
    )

    return results.get("documents", [[]])[0]