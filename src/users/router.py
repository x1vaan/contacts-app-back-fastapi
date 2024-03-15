from fastapi import APIRouter, Depends
from users import service
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from users.dtos import create_user_dto

router = APIRouter(prefix="/users")

@router.get("/")
def users(db : Session = Depends(get_db)):
    return service.users(db)

# @router.post("/create")
# def createUser(user_dto : create_user_dto, db : Session = Depends(get_db)):
#     return service.createUser(user_dto=user_dto, db=db)
