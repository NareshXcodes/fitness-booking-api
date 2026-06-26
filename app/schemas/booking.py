from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


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