from fastapi import APIRouter, Depends, Body, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from ..database import crud, schemas, models
from ..dependencies import get_db, get_current_user
from ..zapiex.zapiex import zapiex_apis

from datetime import datetime, timedelta
from typing import List

router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("/", response_model=schemas.User)
async def create_user_info(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=schemas.User)
async def get_user_info(current_user: models.User = Depends(get_current_user)):
    return current_user


@router.put("/", response_model=schemas.User)
async def update_user_info(
    update_data: schemas.UserUpdate,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return crud.update_user(db, db_user=current_user, update_data=update_data)


@router.delete("/", response_model=schemas.User)
async def delete_user_info(
    current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)
):
    return crud.delete_user(db, db_user=current_user)


# super user 전용 apis
# @router.get("/", response_model=List[schemas.User])
# async def get_users_info(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return crud.get_users(db, skip=skip, limit=limit)
