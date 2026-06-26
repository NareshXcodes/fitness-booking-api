from datetime import datetime
from sqlalchemy import DateTime, Integer, String, ForeignKey, func
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.database import Base

class Booking(Base):
    __tablename__ ="bookings"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    class_id : Mapped[int] = mapped_column(Integer, ForeignKey("fitness_classes.id",ondelete="CASCADE"),nullable=False)
    user_id : Mapped[int] = mapped_column(Integer, ForeignKey("users.id",ondelete="SET NULL"),nullable=False)
    client_name : Mapped[str] = mapped_column(String, nullable=False)
    client_email : Mapped[str] = mapped_column(String, nullable=False)
    booked_at : Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user: Mapped["User"] = relationship(
        "User",
        back_populates="bookings"
    )

    fitness_class: Mapped["FitnessClass"] = relationship(
        "FitnessClass",
        back_populates="bookings"
    )