from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

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