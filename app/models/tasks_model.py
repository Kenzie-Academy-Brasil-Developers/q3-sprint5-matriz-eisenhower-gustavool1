from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from app.configs.database import db
from dataclasses import dataclass 


@dataclass
class TasksModel(db.Model):

    __tablename__ = "tasks"
    id:int = Column(Integer, primary_key = True, unique = True)
    name:str = Column(String(100), nullable = False, unique = True)
    description:str = Column(Text)
    duration:int = Column(Integer)
    importance:int = Column(Integer)
    urgency:int = Column(Integer)


    task = relationship("TaskCategoriesModel", backref="task")

    eisenhower_id = Column(
        Integer,
        ForeignKey("eisenhowers.id"),
        nullable=False
    )

    