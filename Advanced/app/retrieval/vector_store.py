import chromadb

from app.core.config import settings


client = chromadb.PersistentClient(
    path=settings.CHROMA_DB_DIR
)

collection = client.get_or_create_collection(
    name="documents"
)


def add_documents(documents):
    if not documents:
        return {
            "status": "no documents",
            "count": 0
        }

    ids = []
    texts = []

    for i, document in enumerate(documents):
        ids.append(f"doc_{i}")
        texts.append(str(document))

    collection.add(
        ids=ids,
        documents=texts
    )

    return {
        "status": "documents added",
        "count": len(texts)
    }


def search_documents(query: str, k: int = 5):
    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    return results.get("documents", [[]])[0]