from fastapi import APIRouter, Depends, status, Cookie, Response
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Optional
from jose import jwt
from sqlalchemy.orm import Session
from pydantic import ValidationError

from app.core.security import authenticate_user, create_access_token, TOKEN_ALGORITHM
from app.schemas import pyd_token
from app.dependencies import get_db
from app.settings import TOKEN_SECRET_KEY

from datetime import timedelta


ACCESS_TOKEN_EXPIRE_DAYS = 1


router = APIRouter(prefix="/aaa", tags=["aaa"])


@router.post("/token", response_model=pyd_token.Token)
async def login_for_access_token(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    access_token = create_access_token(
        data={"sub": user.email},
        token_secret_key=TOKEN_SECRET_KEY,
        token_algorithm=TOKEN_ALGORITHM,
        expires_delta=access_token_expires,
    )
    response.set_cookie(
        key="access_token", value=f"{access_token}", expires=60 * 60 * 24, httponly=True
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/token")
async def verify_access_token(access_token: Optional[str] = Cookie(None)):
    try:
        jwt.decode(access_token, TOKEN_SECRET_KEY, algorithms=[TOKEN_ALGORITHM])
        return {"valid": True}
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
