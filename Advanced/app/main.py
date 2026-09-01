from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

from dotenv import load_dotenv

from app.workflow.rag import ask_rag
from app.ingestion.service import ingest_pdf
from app.retrieval.vector_store import add_documents

load_dotenv()

app = FastAPI(
    title="Production RAG Assistant",
    description="Production-ready RAG Assistant API",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request model
class QuestionRequest(BaseModel):
    question: str


# Health check
@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "message": "Production RAG Assistant is running"
    }


# Ask question
@app.post("/api/ask")
def ask_question(request: QuestionRequest):
    return ask_rag(request.question)


# Upload and ingest document
@app.post("/api/upload")
async def upload_document(file: UploadFile = File(...)):

    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    contents = await file.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    # Extract text from PDF
    documents = ingest_pdf(file_path)

    # Store extracted documents in ChromaDB
    result = add_documents(documents)

    return {
        "message": "Document uploaded and indexed successfully",
        "filename": file.filename,
        "chunks_added": result["count"]
    }


# Root
@app.get("/")
def root():
    return {
        "message": "Production RAG Assistant API is running"
    }