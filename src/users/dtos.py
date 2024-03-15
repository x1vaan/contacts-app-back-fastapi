from pydantic import BaseModel, EmailStr, Field

class create_user_dto(BaseModel):
    name : str = Field(min_length=1, max_length=40)
    username : str
    email : EmailStr
    password : str

    class Config:
        # le especificamos que será para uso de un ORM
        orm_mode = True