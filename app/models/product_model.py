from sqlalchemy import Column, Integer, String, Float, CheckConstraint
from app.database import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)
    price = Column(Float, CheckConstraint('price>0'), nullable=False)