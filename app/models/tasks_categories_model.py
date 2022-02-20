from app.configs.database import db 
from dataclasses import dataclass
from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from app.models.categories_model import CategoriesModel

from app.models.tasks_model import TasksModel

@dataclass
class TaskCategoriesModel(db.Model):

    __tablename__ = "tasks_categories"
    id:int = Column(Integer, primary_key = True, unique = True)
    
    task_id:TasksModel = Column(
        Integer,
        ForeignKey("tasks.id")
    )

    category_id:CategoriesModel = Column(
        Integer,
        ForeignKey("categories.id")
    )