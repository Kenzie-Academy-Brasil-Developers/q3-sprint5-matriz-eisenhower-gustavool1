from unicodedata import category
from app.configs.database import db
from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from dataclasses import dataclass


@dataclass
class CategoriesModel(db.Model):

    __tablename__ = "categories"

    id:int = Column(Integer, primary_key = True)
    name:str = Column(String(100), nullable = False, unique = True)
    description:str = Column(Text)

    task = relationship("TaskCategoriesModel", backref = "category")