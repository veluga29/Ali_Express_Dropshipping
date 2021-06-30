from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import crud, schemas, models
from ..dependencies import get_db
from ..zapiex.zapiex import zapiex_apis

router = APIRouter(
    tags=["items"]
)


@router.post("/users/{user_id}/items/{product_id}", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, product_id: str, db: Session = Depends(get_db)
):
    product_info = zapiex_apis.get_product(product_id)
    title = product_info['data']['title'].split()[0:2]
    description = product_info['data']['htmlDescription'].split('<strong>●')[1].split('</strong>')[0]
    item = models.Item(title=title, description=description, owner_id=user_id)
    return crud.create_user_item(db=db, db_item=item)


@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
