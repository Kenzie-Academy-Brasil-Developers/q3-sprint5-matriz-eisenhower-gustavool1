from app.configs.database import db 
from dataclasses import dataclass
from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship

@dataclass
class TaskCategoriesModel(db.Model):

    __tablename__ = "tasks_categories"
    id:int = Column(Integer, primary_key = True, unique = True)
    
    task = Column(
        Integer,
        ForeignKey("tasks.id")
    )

    category = Column(
        Integer,
        ForeignKey("categories.id")
    )