import os
from openai import OpenAI
from logging_config import logger

class OpenAIRepository:
  def __init__(self):
    try:
      openai_api_key = os.getenv('OPEN_AI_KEY')
      openai_project_id = os.getenv('OPEN_AI_PROJECT_ID')
      
      self.openai_client = OpenAI(
        api_key=openai_api_key,
        project=openai_project_id
      )

      logger.info('OpenAI Client created!')
    except KeyError:
      logger.error('Error when trying to creat an OpenAI client: ', KeyError)

  def ask_question(self, prompt: str):
    try:
      logger.info(f"Executing OpenAI assistant with the prompt: {prompt}")

      output = self.openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
          {
            "role": "user", 
            "content": prompt
          }
        ],
        stream=True
      )

      response_text = ""
      
      for chunk in output:
        if chunk.choices[0].delta.content is not None:
            response_text += chunk.choices[0].delta.content


      return { 'data': response_text }
    except KeyError:
      logger.error("OpenAI assistant failed with the error: ", KeyError)
      return "Error occurred"

    except Exception:
      logger.error("Unexpected error: ", Exception)
      return "Unexpected error occurred"