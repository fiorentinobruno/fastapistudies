from fastapi import APIRouter, Depends, HTTPException, Path
from ..models import Todos, Users
from ..database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from starlette import status
from pydantic import BaseModel, Field
from .auth import get_current_user
from passlib.context import CryptContext

router = APIRouter(prefix="/user", tags=["user"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str
    confirm_password: str

@router.get("/info", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    info = db.query(Users).filter(Users.id == user.get("id")).first()

    return info

@router.put("/changepassword", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependency, db: db_dependency, data: ChangePasswordRequest):
    if user is None: 
        raise HTTPException(status_code=401, detail="Authorization failed")

    db_user = db.query(Users).filter(Users.id == user.get("id")).first()
    if not bcrypt_context.verify(data.current_password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    if not (data.new_password == data.confirm_password):
        raise HTTPException(status_code=401)
    
    db_user.hashed_password = bcrypt_context.hash(data.new_password)
    db.commit()

    
    

    

    
    
