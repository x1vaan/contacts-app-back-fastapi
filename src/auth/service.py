from sqlalchemy.orm import Session
from users.dtos import create_user_dto
from users import service as user_service
from fastapi import HTTPException

def register(user_dto : create_user_dto, db : Session):
    user_already_created = user_service.getUserByEmail(user_dto.email, db)
    if user_already_created:
        raise HTTPException(status_code=400, detail="User Already exists.")
    
    user = user_service.createUser(user_dto, db)
    return user