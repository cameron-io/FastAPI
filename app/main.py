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

engine = create_engine(env.get('DATABASE_URI'))
Base.metadata.create_all(bind=engine)

# Middleware
from fastapi import Request
from .middleware.auth import extract_claims_from_request

@app.middleware("http")
async def auth_pre_handle(request: Request, call_next):
    user = extract_claims_from_request(request)
    request.path_params['user'] = user
    return await call_next(request)

# Routes
from .http.user import read_item, read_root
