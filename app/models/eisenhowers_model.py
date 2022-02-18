from dataclasses import dataclass
from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship
from app.configs.database import db

@dataclass
class EisenhowersModel(db.Model):

    __tablename__ = "eisenhowers" 

    id:int = Column(Integer, primary_key = True)
    type:str = Column(String(100))

    eisenhower_id = relationship("TasksModel", backref="eisenhower_id") 