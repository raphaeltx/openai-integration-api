from fastapi import APIRouter, HTTPException
from src.services.question_service import QuestionService
from logging_config import logger

router = APIRouter()

@router.post("/ask-question")
async def ask_question(payload: dict):
    prompt = payload.get("text")

    if not prompt:
        raise HTTPException(status_code=400, detail="No prompt provided")

    try:
        service = QuestionService();
        response = service.ask_question(prompt)
        return response
    except Exception as e:
        logger.error("OpenAI assistant failed with the error: ", e)
        raise HTTPException(status_code=500, detail=f"Error occurred: {str(e)}")