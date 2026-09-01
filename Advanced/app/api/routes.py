from fastapi import APIRouter
from app.models.schemas import QuestionRequest, AnswerResponse
from app.workflow.rag import ask_rag

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    return ask_rag(request.question)