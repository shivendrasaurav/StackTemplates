from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session

from .config import newserviceconfig
from .db import get_db_conn, create_user, get_user
from .models import UserBase, UserCreate, UserResponse # , UserORM || Include this if you want to use ORM based queries

router = APIRouter()
AUTH_KEY= newserviceconfig.SERVICE_AUTH_KEY

def get_token_from_header(auth_key: str = Header(..., alias="Service-Auth-Key")):
    if not auth_key:
        raise HTTPException(status_code=401, detail="AuthKey header is missing")
    return auth_key

@router.get("/getauthtoken/")
async def get_auth_key():
    return {
        "auth_key": AUTH_KEY
    }


# ============== Using Direct Database Connection ============== #

@router.get("/createnewuser/")
async def create_new_user(auth_key: str = Depends(get_token_from_header)):
    if auth_key != AUTH_KEY:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    # add API endpoint operations here
    ops = create_user("lol", "lol")
    return {
        "message": "default response from create new user route"
    }


@router.get("/getuserwithid/{userid}")
async def get_user_data(userid: int, auth_key: str = Depends(get_token_from_header)):
    if auth_key != AUTH_KEY:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    # add API endpoint operations here
    ops = get_user(userid)
    return {
        "message": "default response from get user with id route " + str(userid)
    }


# ============== Using SQLAlchemy ORM ============== #

"""
Enable If You Want To Use ORM Based Database Operations

from .db_orm import get_db

@router.post("/users-orm/", response_model=UserBase)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserORM(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users-orm/{user_id}", response_model=UserBase)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserORM).filter(UserORM.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

"""