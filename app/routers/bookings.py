from app.logger import logger
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from app.database import get_db
from app.dependencies import get_current_user
from app.models.booking import Booking
from app.models.fitness_class import FitnessClass
from app.models.user import User
from app.schemas.booking import BookingCreate, BookingRead
from app.services.booking_service import book_class


router = APIRouter(tags=['Bookings'])


@router.post('/book',response_model= BookingRead,status_code=status.HTTP_201_CREATED)
def create_booking(new_booking : BookingCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    booking = book_class(
            class_id = new_booking.class_id,
            user_id = current_user.id,
            client_name = new_booking.client_name,
            client_email = new_booking.client_email,
            db = db 
        )
    logger.info(f"{current_user.email} booked class '{booking.fitness_class.name}'.")

    return BookingRead(
        id = booking.id,
        class_id = booking.class_id,
        client_name= booking.client_name,
        client_email=booking.client_email,
        booked_at= booking.booked_at,
        class_name = booking.fitness_class.name,
        dateTime = booking.fitness_class.date_time,
        instructor= booking.fitness_class.instructor
    )

@router.get("/bookings", response_model=List[BookingRead])
def get_bookings(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    bookings = db.query(Booking).filter(Booking.user_id == current_user.id).all()

    logger.info(f"{current_user.email} viewed their bookings.")
    return [
        BookingRead(
            id=booking.id,
            class_id=booking.class_id,
            client_name=booking.client_name,
            client_email=booking.client_email,
            booked_at=booking.booked_at,
            class_name=booking.fitness_class.name,
            dateTime=booking.fitness_class.date_time,
            instructor=booking.fitness_class.instructor,
        )
        for booking in bookings
    ]


