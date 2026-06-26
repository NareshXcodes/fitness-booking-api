from email.policy import HTTP
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app.models.fitness_class import FitnessClass
from app.models.user import User
from app.schemas.class_ import ClassCreate, ClassRead
from zoneinfo import ZoneInfo
from datetime import datetime


router = APIRouter(prefix="/classes",tags=['Fitness Classes'])


IST = ZoneInfo("Asia/Kolkata")


@router.post("/",response_model=ClassRead,status_code=status.HTTP_201_CREATED)
def create_classes(class_data: ClassCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):

    if class_data.availableSlots <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Available slots must be greater than 0."
        )

    dt = class_data.dateTime

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=IST)
    else:
        dt = dt.astimezone(IST)

    dt = dt.replace(tzinfo=None)

    
    ist_time = class_data.dateTime.astimezone(IST)
    if class_data.dateTime <= datetime.now(class_data.dateTime.tzinfo):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Class date must be in the future."
        )

    fc = FitnessClass(
        name=class_data.name,
        instructor=class_data.instructor,
        date_time=dt,
        available_slots=class_data.availableSlots,
        created_by=current_user.id,
    )

    db.add(fc)
    db.commit()
    db.refresh(fc)
    return ClassRead(
        id = fc.id,
        name = fc.name,
        instructor=fc.instructor,
        dateTime = fc.date_time,
        availableSlots = fc.available_slots
    )


@router.get('/',response_model=List[ClassRead])
def get_classes(db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    now_ist = datetime.now(IST).replace(tzinfo=None)

    classes = db.query(FitnessClass).filter(FitnessClass.created_by == current_user.id,FitnessClass.date_time >= now_ist).order_by(FitnessClass.date_time).all()

    return [
        ClassRead(
            id=c.id,
            name=c.name,
            dateTime=c.date_time,
            instructor=c.instructor,
            availableSlots=c.available_slots,
        )
        for c in classes
    ]


