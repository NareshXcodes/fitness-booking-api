from datetime import datetime, timezone
from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.database import Base
from typing import List


class FitnessClass(Base):
    __tablename__ = "fitness_classes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    instructor: Mapped[str] = mapped_column(String(100), nullable=False)
    date_time: Mapped[datetime] = mapped_column(DateTime(timezone.utc), nullable=False)
    available_slots : Mapped[int] = mapped_column(Integer, nullable=False)
    created_by : Mapped[int] = mapped_column(Integer, ForeignKey("users.id",ondelete="CASCADE"),nullable=False)

    user : Mapped["User"] = relationship(
        "User",
        back_populates="fitness_classes"
    )

    bookings : Mapped[List["Booking"]] = relationship(
        "Booking",
        back_populates="fitness_class",
        cascade="all, delete-orphan"
    )