from fastapi import APIRouter, Depends, Query
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from ..database import crud, schemas, models
from ..dependencies import get_db
from ..zapiex.zapiex import zapiex_apis

from datetime import datetime, timedelta
from typing import List

router = APIRouter(prefix="/", tags=["accounts"])
