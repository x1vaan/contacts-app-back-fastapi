from pydantic import BaseModel

class userDto(BaseModel):
    name : str
    username : str
    email : str
    password : str

    class Config:
        # le especificamos que será para uso de un ORM
        orm_mode = True