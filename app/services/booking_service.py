from datetime import datetime
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.booking import Booking
from app.models.fitness_class import FitnessClass
from zoneinfo import ZoneInfo


IST = ZoneInfo("Asia/Kolkata")

def book_class(class_id : int, user_id : int, client_name : str, client_email : str, db: Session ):
    fitness_class = db.query(FitnessClass).filter(FitnessClass.id == class_id).first()

    if not fitness_class:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fitness Class not found"
        )

    if fitness_class.available_slots <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No slots available."
        )

    now_ist = datetime.now(IST).replace(tzinfo=None)

    if fitness_class.date_time <= now_ist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot book an expired class."
        )

    booking = db.query(Booking).filter(Booking.class_id == class_id,Booking.user_id == user_id).first()

    if booking:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="You have already booked this class."
        )

    fitness_class.available_slots -= 1

    booking = Booking(
        class_id=class_id,
        user_id=user_id,
        client_name=client_name,
        client_email=client_email,
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)

    return booking
        