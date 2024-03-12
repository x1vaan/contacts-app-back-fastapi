from fastapi import APIRouter, Depends
from users import service
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from users.dtos import userDto

router = APIRouter(prefix="/users")

@router.get("/")
def users(db : Session = Depends(get_db)):
    return service.users(db)

@router.post("/login")
def postUsers(user_dto : userDto, db : Session = Depends(get_db)):
    return service.postUser(user_dto=user_dto, db=db)
