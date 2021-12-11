from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.crud import crud_user
from app.schemas import pyd_user
from app.models import model_user
from app.dependencies import get_db, get_current_user


router = APIRouter(prefix="/me", tags=["me"])


@router.post("/", response_model=pyd_user.User)
def create_me(user: pyd_user.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )
    return crud_user.create_user(db=db, user=user)


@router.get("/", response_model=pyd_user.User)
def read_me(current_user: model_user.User = Depends(get_current_user)):
    return current_user


@router.patch("/", response_model=pyd_user.User)
def update_me(
    update_data: pyd_user.UserUpdate,
    current_user: model_user.User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return crud_user.update_user(db, db_user=current_user, update_data=update_data)


@router.delete("/", response_model=pyd_user.User)
def delete_me(
    current_user: model_user.User = Depends(get_current_user), db: Session = Depends(get_db)
):
    return crud_user.delete_user(db, db_user=current_user)
