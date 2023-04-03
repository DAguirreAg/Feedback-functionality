from fastapi import APIRouter, Depends, HTTPException
from .schemas import Feedback
from sqlalchemy.orm import Session
from dependencies import get_db
from sql_app import models


router = APIRouter(
    #prefix="/",
    tags=["Feedbacks"],
    responses={404: {"description": "Not found"}}
)

@router.post('/feedback')
def add_feedback(feedback: Feedback, db: Session = Depends(get_db)):
    
    # Get values
    email = feedback.email
    feedbackText = feedback.feedback

    # Add feedback to the DB
    feedback = models.Feedback(email=email, feedback=feedbackText)
    db.add(feedback)
    db.commit()

    return {'detail': 'Feedback added successfully.'}