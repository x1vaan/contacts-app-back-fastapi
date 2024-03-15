from fastapi import APIRouter, Depends
from auth import service
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from users.dtos import create_user_dto

router = APIRouter(prefix="/auth")

@router.post("/register")
def register(user_dto : create_user_dto, db : Session = Depends(get_db)):
    return service.register(user_dto, db)