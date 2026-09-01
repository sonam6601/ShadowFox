from pathlib import Path
from pypdf import PdfReader


def ingest_pdf(file_path: str):
    path = Path(file_path)

    reader = PdfReader(str(path))

    chunks = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():
            chunks.append({
                "text": text,
                "metadata": {
                    "source": path.name,
                    "page": page_number
                }
            })

    return chunks