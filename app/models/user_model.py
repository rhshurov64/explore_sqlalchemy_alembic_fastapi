from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy_utils import EmailType


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(EmailType, unique=True, nullable=False)
    name =  Column(String(255), nullable=True)