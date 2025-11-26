from pydantic import BaseModel, Field
from datetime import date

class DayUpdatePayload(BaseModel):
    date: str
    value: int = Field(..., ge=0, le=100)
    last_updated: str

class DateModel(BaseModel):
    day: date