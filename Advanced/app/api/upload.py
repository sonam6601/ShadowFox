from pathlib import Path

from fastapi import APIRouter, File, UploadFile

from app.ingestion.service import ingest_pdf
from app.retrieval.vector_store import add_documents
from app.core.config import settings


router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    upload_dir = Path(settings.upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / file.filename

    content = await file.read()
    file_path.write_bytes(content)

    chunks = ingest_pdf(str(file_path))
    add_documents(chunks)

    return {
        "message": "Document uploaded successfully",
        "filename": file.filename,
        "chunks": len(chunks),
    }