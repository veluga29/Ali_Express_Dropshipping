from fastapi import APIRouter

from ..zapiex import zapiex

router = APIRouter(
    tags=["search"]
)

@router.get("/search/{text}")
async def search_items(text: str):
    return zapiex.search_products(text)