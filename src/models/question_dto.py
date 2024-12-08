from pydantic import BaseModel

class QuestionDTO(BaseModel):
    text: str