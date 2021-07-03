from re import search
from typing import List

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
import json

from ..database import crud, schemas, models
from ..dependencies import get_db
from ..zapiex.zapiex import zapiex_apis

router = APIRouter(
    tags=["search"]
)

'''
1. Store SearchText <-> ProductList one-to-one relationship
2. DB query grammar & DB create grammar modification
3. Implementation steps should be modify
'''

@router.post("/search/", response_model=schemas.ProductList)
# @router.post("/search/")
async def search_items_by_text(text: str, page: int, db: Session = Depends(get_db)):
    try:
        search_text = crud.get_search_text_and_page(db, text=text, page=page)
        # 이미 검색한 기록이 있으면 db에서 꺼내 보여줌
        if search_text:
            return search_text.product_list
        search_info = zapiex_apis.search_products(text, page)  # Zapiex API 호출
        if search_info["statusCode"] == 200:
            search_text = crud.create_search_text(db=db, text=text, page=page)  # search_text 테이블에 저장
            information = search_info["data"]
            return crud.create_searched_products(db=db, information=information, search_text_id=search_text.id)
        else:
            raise HTTPException(detail={"error_code": 1}, status_code=400)
    except Exception as e:
        # raise HTTPException(detail=e, status_code=400)
        print(e)