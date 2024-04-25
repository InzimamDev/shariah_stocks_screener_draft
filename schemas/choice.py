

class ChoiceBase(BaseModel):
  choice_text: str
  is_correct: bool


class QuestionBase(BaseModel):
  question_text: str
  choices: List[ChoiceBase]
