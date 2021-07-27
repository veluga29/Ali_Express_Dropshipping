from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session
from pydantic import ValidationError

from .database import crud, schemas
from .database.database import SessionLocal
from .settings import TOKEN_SECRET_KEY

TOKEN_ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="aaa/token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, TOKEN_SECRET_KEY, algorithms=[TOKEN_ALGORITHM])
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.get_user_by_email(db, email=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
