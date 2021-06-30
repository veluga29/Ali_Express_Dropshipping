from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json

from ..database import crud, schemas, models
from ..dependencies import get_db
from ..zapiex.zapiex import zapiex_apis

router = APIRouter(
    tags=["search"]
)

@router.post("/search/", response_model=List[schemas.ProductLists])
async def create_search_items(text: str, db: Session = Depends(get_db)):
    db_text = crud.get_search_text(db, text=text)
    # 이미 검색한 기록이 있으면 db에서 꺼내 보여줌
    if db_text:
        return crud.get_searched_products(db, db_text_id=db_text.id)
    search_text = models.SearchText(text=text)
    created_search_text = crud.create_search_text(db=db, db_item=search_text)  # search_text 테이블에 저장
    search_info = zapiex_apis.search_products(text)  # Zapiex API 호출
    searched_products = search_info["data"]["items"]
    p_list = []  # 네이밍 다시 신경써야할 것 같습니다
    for product in searched_products:  # 하나씩 각각 저장하는게 속도적으로 단점이 되진 않을까요?
        product_lists = models.ProductLists(product=product, search_text_id=created_search_text.id)
        p_list.append(crud.create_searched_products(db=db, db_item=product_lists))  # products 테이블에 저장
    return p_list