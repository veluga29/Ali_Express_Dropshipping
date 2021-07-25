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


@router.post("/", response_model=schemas.UserOut)
async def create_user_info(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email, user_id=user.user_id)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=schemas.UserOut)
async def get_user_info(current_user: schemas.UserInDB = Depends(get_current_user)):
    return current_user


@router.put("/", response_model=schemas.UserOut)
async def update_user_info(
    db: Session = Depends(get_db),
    email: str = Body(None),  # validation
    password: str = Body(None),
    first_name: str = Body(None),
    last_name: str = Body(None),
    current_user: schemas.UserUpdate = Depends(get_current_user),
):
    # current_user_data = jsonable_encoder(current_user)
    # user_in = schemas.UserUpdate(**current_user_data)
    if email is not None:
        current_user.email = email
    if password is not None:  # hashed
        current_user.password = password
    if first_name is not None:
        current_user.first_name = first_name
    if last_name is not None:
        current_user.last_name = last_name
    user = crud.update_user(db, current_user=current_user, user_in=user_in)  # **user_info
    return user


@router.delete("/", response_model=schemas.UserOut)
async def delete_user_info(
    db: Session = Depends(get_db), current_user: schemas.UserDelete = Depends(get_current_user)
):
    return crud.delete_user(db, id=current_user.id)


# super user 전용 apis
# @router.get("/", response_model=List[schemas.UserOut])
# async def get_users_info(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return crud.get_users(db, skip=skip, limit=limit)
