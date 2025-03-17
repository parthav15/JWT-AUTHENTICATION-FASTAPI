from typing import Optional

from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
from schemas import Register


def get_user(username: str) -> Optional[User]:
    with SessionLocal() as db:
        return db.query(User).filter(User.username == username).one_or_none()


def add_user(user: Register) -> Optional[User]:
    db_user = User(**user.dict())
    with SessionLocal() as db:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    return db_user