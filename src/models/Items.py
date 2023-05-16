from sqlalchemy import Column, Integer, String
from src.common.database import Database


class Item(Database.Base_model):
    __tablename__ = "items"

    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    image = Column(String(100), nullable=True)