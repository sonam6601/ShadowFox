from pathlib import Path

from app.ingestion.loader import load_pdf
from app.ingestion.chunker import split_text


def ingest_pdf(file_path: str) -> list[str]:
    text = load_pdf(file_path)

    if not text:
        return []

    chunks = split_text(text)

    return chunks