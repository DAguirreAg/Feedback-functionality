from pydantic import BaseModel, EmailStr, validator, Field
from typing import Union

class Feedback(BaseModel):
    email: EmailStr | None = None
    feedbackText: str = Field(default=None, min_length=25, max_length=300)