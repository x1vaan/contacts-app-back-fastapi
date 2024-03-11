from pydantic import BaseModel

class userDto(BaseModel):
    name : str
    age : int