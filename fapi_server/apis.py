from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from models import create_user as raw_create_user, get_user as raw_get_user
from ormmodels import create_user as orm_create_user, get_user as orm_get_user
from db import get_db
from config import config

router = APIRouter()

auth_key= config.APP_AUTH_KEY

# Checks for App-Auth-Key header in rest api request
def get_token_from_header(auth_key: str = Header(..., alias="App-Auth-Key")):
    if not auth_key:
        raise HTTPException(status_code=401, detail="AuthKey header is missing")
    return auth_key

@router.get("/getauthtoken/")
async def get_auth_key():
    return {
        "auth_key": AUTH_KEY
    }

@router.post("/create_user/")
async def api_create_user(name: str, email: str, auth_key: str = Depends(get_token_from_header)):
    user = raw_create_user(name, email)
    return {"id": user}

@router.get("/get_user/{user_id}")
async def api_get_user(user_id: int, auth_key: str = Depends(get_token_from_header)):
    return str(user_id)
    user = raw_get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}
