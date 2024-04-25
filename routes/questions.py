from fastapi import APIRouter, Depends, HTTPException
from typing import List, Annotated
from ..models import Questions, Choices  # Assuming models are in a separate `models.py` file
from ..database import SessionLocal, get_db
from ..schemas.question import QuestionBase
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/questions/", response_model=Questions)
async def create_question(question: QuestionBase, db: db_dependency = Depends(get_db)):
    db_question = Questions(question_text=question.question_text)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    for choice in question.choices:
        db_choice = Choices(choice_text=choice.choice_text, is_correct=choice.is_correct, question_id=db_question.id)
        db.add(db_choice)
    db.commit()
    return db_question
