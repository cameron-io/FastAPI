from dotenv import load_dotenv
from .utils import env

if (load_dotenv() != True):
    exit('Failed to initialize environment')

# App
from fastapi import FastAPI

app = FastAPI()

# DB
from sqlalchemy import create_engine
from .models import Base

engine = create_engine(env.getvar('DATABASE_URI'))
Base.metadata.create_all(bind=engine)

# Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from .middleware.auth import AuthBackend

app.add_middleware(AuthenticationMiddleware, backend=AuthBackend())

# Routes
from app.routers import user
app.include_router(user.router)
