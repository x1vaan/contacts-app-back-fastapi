#Inits the FastAPI app
from fastapi import FastAPI
from users.router import router as users_router
from auth.router import router as auth_router
from users import models as user_models
from database import Base, engine

try:
    user_models.Base.metadata.create_all(engine)
except Exception as e:
    print(e)

app = FastAPI()
app.include_router(users_router)
app.include_router(auth_router)