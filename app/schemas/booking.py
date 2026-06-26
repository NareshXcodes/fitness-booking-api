from datetime import datetime
from app.config import IST
from pydantic import BaseModel, ConfigDict, EmailStr,field_serializer


class BookingCreate(BaseModel):
    class_id : int
    client_name : str
    client_email : EmailStr

class BookingRead(BaseModel):
    id : int
    class_id : int
    client_name : str
    client_email : EmailStr
    booked_at : datetime
    class_name : str
    dateTime : datetime
    instructor : str
    model_config = ConfigDict(from_attributes=True)
    @field_serializer("booked_at")
    def serialize_booked_at(self, value: datetime):
        if value.tzinfo is None:
            value = IST.localize(value)
        return value.isoformat()

    @field_serializer("dateTime")
    def serialize_class_time(self, value: datetime):
        if value.tzinfo is None:
            value = IST.localize(value)
        return value.isoformat()