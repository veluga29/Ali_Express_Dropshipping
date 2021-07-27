from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.crud import crud_user
from app.schemas import user
from app.models.user import User
from app.dependencies import get_db, get_current_user


router = APIRouter(prefix="/accounts", tags=["accounts"])


@router.post("/", response_model=user.User)
async def create_user_info(user: user.UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )
    return crud_user.create_user(db=db, user=user)


@router.get("/", response_model=user.User)
async def get_user_info(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("/", response_model=user.User)
async def update_user_info(
    update_data: user.UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return crud_user.update_user(db, db_user=current_user, update_data=update_data)


@router.delete("/", response_model=user.User)
async def delete_user_info(
    current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    return crud_user.delete_user(db, db_user=current_user)


# super user 전용 apis
# @router.get("/", response_model=List[user.User])
# async def get_users_info(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return crud_user.get_users(db, skip=skip, limit=limit)
