from src.repositories.openai_repository import OpenAIRepository

class QuestionService:
  def __init__(self):
    self.openai_repository = OpenAIRepository()

  def ask_question(self, prompt: str) -> dict:
    response = self.openai_repository.ask_question(prompt)

    return response