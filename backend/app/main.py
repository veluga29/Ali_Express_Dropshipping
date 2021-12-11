from fastapi import FastAPI

# from fastapi_pagination import add_pagination
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import accounts, authentication, products
from app.settings import CORS_ORIGIN


app = FastAPI()

origins = eval(CORS_ORIGIN)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# 데이터 베이스 이니셜라이즈
Base.metadata.create_all(bind=engine)

# 라우터 정의
app.include_router(products.router)
app.include_router(authentication.router)
app.include_router(accounts.router)

# add_pagination(app)


@app.get("/")
async def root():
    return {"message": "Welcome to Ali Express Dropshipping service!"}
