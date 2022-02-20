from flask import current_app
from app.models.eisenhowers_model import EisenhowersModel

def populating_db():
    session = current_app.db.session
    values = [
        'Do It First',
        'Delegate It',
        'Schedule It',
        'Delete It'
    ]

    for value in values:
        eisenhower = EisenhowersModel(type=value)
        session.add(eisenhower)
    session.commit()