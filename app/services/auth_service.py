from jose import JWTError , jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from app.config import settings


pwd_context = CryptContext(schemes = ["bcrypt"],deprecated="auto")

def hash_password(plain):
    return pwd_context.hash(plain)

def verify_password(plain: str, hashed: str):
    return pwd_context.verify(plain,hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=int(settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, str(settings.SECRET_KEY), algorithm=str(settings.ALGORITHM))

    return encoded_jwt


def verify_access_token(token: str,credentials_exception):
    try:
        payload = jwt.decode(token, str(settings.SECRET_KEY), algorithms=[str(settings.ALGORITHM)])
        subject: str = payload.get("sub")
        if subject is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return subject


