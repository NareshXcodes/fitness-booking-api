from datetime import datetime
from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.database import Base
from typing import List
from zoneinfo import ZoneInfo



IST = ZoneInfo("Asia/Kolkata")


class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name : Mapped[str]= mapped_column(String, unique=True, index=True, nullable=False)
    email : Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    password : Mapped[str] = mapped_column(String, nullable=False)
    created_at : Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(IST).replace(tzinfo=None),nullable=False)

    #relationship
    fitness_classes : Mapped[List["FitnessClass"]] = relationship(
        "FitnessClass",
        back_populates="user"
    )

    bookings : Mapped[List["Booking"]] = relationship(
        "Booking",
        back_populates="user"
    )