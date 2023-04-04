from pydantic import BaseModel, EmailStr, validator
from typing import Union

class Feedback(BaseModel):
    email: EmailStr | None = None
    feedbackText: str