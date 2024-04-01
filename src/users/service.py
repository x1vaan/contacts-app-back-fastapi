from sqlalchemy.orm import Session
from users.models import User
from users.dtos import create_user_dto

def users(db : Session): 
    users = db.query(User).all()
    return users

def createUser(user_dto : create_user_dto, db : Session):
    user = User(name=user_dto.name, username= user_dto.username, email=user_dto.email, password= user_dto.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def getUserByEmail(email : str, db : Session):
    user = db.query(User).filter(User.email == email).all()
    return user