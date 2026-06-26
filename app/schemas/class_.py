from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, field_serializer
from datetime import datetime
from app.config import IST

class ClassCreate(BaseModel):
    name : str
    dateTime : datetime
    instructor : str
    availableSlots : int

class ClassRead(BaseModel):
    id : int
    name : str
    dateTime : datetime
    instructor : str
    availableSlots : int = Field(gt=0)
    model_config = ConfigDict(from_attributes=True)
    @field_serializer("dateTime")
    def serialize_datetime(self, value: datetime):
        if value.tzinfo is None:
            value = value.replace(tzinfo=IST)
        else:
            value = value.astimezone(IST)
        return value.isoformat()