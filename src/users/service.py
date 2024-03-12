from sqlalchemy.orm import Session
from users.models import User
from users.dtos import userDto

def users(db : Session): 
    users = db.query(User).all()
    return users

def postUser(user_dto : userDto, db : Session):
    user = User(name=user_dto.name, username= user_dto.username, email=user_dto.email, password= user_dto.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user