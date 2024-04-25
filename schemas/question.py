from pydantic import BaseModel
from ..schemas.choice import ChoiceBase

class QuestionBase(BaseModel):
  question_text: str
  choices: List[ChoiceBase]
