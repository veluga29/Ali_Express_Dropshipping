from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..database import crud, schemas
from ..dependencies import get_db
from ..settings import TOKEN_SECRET_KEY

from datetime import timedelta

TOKEN_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1


router = APIRouter(prefix="/aaa", tags=["aaa"])


@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user_id or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(days=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.user_id, "email": user.email},
        token_secret_key=TOKEN_SECRET_KEY,
        token_algorithm=TOKEN_ALGORITHM,
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}
