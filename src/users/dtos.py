from pydantic import BaseModel

class create_user_dto(BaseModel):
    name : str
    username : str
    email : str
    password : str

    class Config:
        # le especificamos que será para uso de un ORM
        orm_mode = True