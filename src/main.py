#Inits the FastAPI app
from fastapi import FastAPI
from users.router import router as users_router

app = FastAPI()

app.include_router(users_router)