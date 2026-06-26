from fastapi import FastAPI
from app.database import Base , engine
from app.models.user import User
from app.models.booking import Booking
from app.models.fitness_class import FitnessClass
from app.routers import auth, bookings, classes

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Fitness Booking API"
    }

app.include_router(auth.router)
app.include_router(classes.router)
app.include_router(bookings.router)