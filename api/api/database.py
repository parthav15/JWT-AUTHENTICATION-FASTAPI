from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./auth.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

Base.metadata.create_all(bind=engine)


# from datetime import datetime
# from sqlalchemy import create_engine, Column, DateTime, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from utils import get_password_hash

# DATABASE_URL = "sqlite:///./auth.db"

# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# class Model(Base):
#     __abstract__ = True
#     __tablename__ = ""

#     id: int = Column(Integer, primary_key=True, autoincrement=True)
#     created: datetime = Column(DateTime, default=datetime.utcnow, nullable=False)
#     updated: datetime = Column(
#         DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
#     )

# class User(Model):
#     __tablename__ = "user"

#     first_name: str = Column(String(length=32), nullable=False)
#     last_name: str = Column(String(length=32), nullable=False)
#     username: str = Column(String(length=32), nullable=False, unique=True, index=True)
#     password: str = Column(String(length=64), nullable=False)
#     email: str = Column(String(length=64), nullable=False, unique=True)
#     phone_number: str = Column(String(length=32), nullable=False)
#     address: str = Column(String(length=64), nullable=False)

#     def __init__(self, password: str, **kwargs):
#         super(User, self).__init__(**kwargs)
#         self.generate_password_hash(password)

#     def generate_password_hash(self, password: str) -> None:
#         self.password = get_password_hash(password)

# Base.metadata.create_all(bind=engine)

