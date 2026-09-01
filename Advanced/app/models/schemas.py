def search_documents(query: str, k: int = 5):
    # Check if collection has any documents
    count = collection.count()

    if count == 0:
        return []

    # Do not request more documents than available
    k = min(k, count)

    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    return results.get("documents", [[]])[0]