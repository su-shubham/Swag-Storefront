from fastapi import APIRouter,Depends
from db import get_session
from sqlmodel import Session
from models import User
from schemas import UserCreate

router = APIRouter(tags=["User"])


@router.post("/user")
async def create_user(user:UserCreate,session:Session = Depends(get_session)):
    user = User.from_orm(user)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
