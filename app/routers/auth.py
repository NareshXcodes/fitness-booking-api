from fastapi import APIRouter , HTTPException , status ,Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.logger import logger
from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.auth import SignupRequest, SignupResponse, TokenResponse
from app.services.auth_service import create_access_token, hash_password, verify_password


router = APIRouter(prefix="/auth" ,tags=["Authentication"])

@router.post("/login", response_model=TokenResponse)
def login(user_credential : OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_credential.username).first()

    if not user or not verify_password(user_credential.password, user.password):
        logger.warning(f"Failed login attempt for: {user_credential.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    access_token = create_access_token(data = {"sub": user.email})
    logger.info(f"User logged in: {user.email}")
    return {"access_token" : access_token , "token_type" : "bearer"}
    

    
@router.post("/signup",response_model=SignupResponse, status_code = status.HTTP_201_CREATED)
def register(new_user : SignupRequest, db:Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == new_user.email).first()

    if existing_user:
        logger.warning(f"Signup failed. Email already exists: {new_user.email}")
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail="Email already taken"
        )

    new_user.password = hash_password(new_user.password)
    user = User(**new_user.model_dump())

    db.add(user)
    db.commit()
    db.refresh(user)
    logger.info(f"New user registered: {user.email}")
    return SignupResponse(
        name = user.name,
        id = user.id,
        email = user.email,
        created_at= user.created_at
    )


# @router.get("/me")
# def current_logged_in_status(current_user : User = Depends(get_current_user)):
#     return current_user