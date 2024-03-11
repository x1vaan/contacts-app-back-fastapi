#Inits the FastAPI app
from fastapi import FastAPI
from users.router import router as users_router
from database import Base, engine

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print(e)

app = FastAPI()
app.include_router(users_router)
