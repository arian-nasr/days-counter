from pydantic import BaseModel, Field

class DayUpdatePayload(BaseModel):
    date: str
    value: int = Field(..., ge=0, le=100)
    last_updated: str