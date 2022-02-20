from http import HTTPStatus
from app.models.eisenhowers_model import EisenhowersModel
from flask import current_app
from app.models.categories_model import CategoriesModel
from app.models.tasks_categories_model import TaskCategoriesModel
from werkzeug.exceptions import BadRequest
def validating_body(importance, urgency):
    invalid_body = []

    valid_body = {
      "importance": [1, 2],
      "urgency": [1, 2]
    }

    if importance not in [1,2] or urgency not in [1,2]:

        received_options = {
        "importance": importance,
        "urgency": urgency
        }
        raise BadRequest(description= {
            "msg":{
            "valid_options":valid_body,
            "recieved_options":received_options
            }
        })

    return False


def checking_repeated_categories(categories):
    non_repeated_categories = []
    for categorie in categories:
        categorie_exists = CategoriesModel.query.filter(CategoriesModel.name == categorie).first()

        if not categorie_exists:
            non_repeated_categories.append(categorie)
                
    return non_repeated_categories

def finding_classfication(importance:int, urgency:int):
    eisenhower = None
    if importance == 1 and urgency == 1:
        eisenhower = EisenhowersModel.query.filter(EisenhowersModel.type == "Do It First" ).first()
        
    if importance == 1 and urgency == 2:
        eisenhower = EisenhowersModel.query.filter(EisenhowersModel.type == "Delegate It").first()
        
    if importance == 2 and urgency == 1:
        eisenhower = EisenhowersModel.query.filter(EisenhowersModel.type == "Schedule It").first()
        
    if importance == 2 and urgency == 2:
        eisenhower = EisenhowersModel.query.filter(EisenhowersModel.type == "Delete It").first()
        
    return eisenhower



def creating_category(categories):
    session = current_app.db.session
    created_categories = []
    for categorie_to_add in categories:
        categorie = CategoriesModel(name=categorie_to_add)
        session.add(categorie)
        session.commit()
        created_categories.append(categorie)
    return created_categories

    
def creating_tasks_categories(categorys_ids, task_id):
    session = current_app.db.session

    for id in categorys_ids:
        task_categorie = TaskCategoriesModel(category_id = id, task_id = task_id)
        session.add(task_categorie)

    session.commit()


def validating_update(data):
    allowed_fields = ["name", "description", "duration", "classification", "importance", "urgency", "categories"]
    allowed_values = [1,2]

    valid_body = {
        "importance": [1, 2],
        "urgency": [1, 2]
    }
    received_options = {
        "importance": data.get("importance", None),
        "urgency": data.get("urgency", None)
    }

    msg = {
        "msg":{
        "valid_options":valid_body,
        "recieved_options":received_options
        }
    }

    not_allowed_fields = [key for key in data.keys() if key not in allowed_fields]
    
    if not_allowed_fields:
        raise BadRequest(description={"error":f"One field or morre not allowed : { not_allowed_fields } "})
    
    if data.get("importance") and data.get("importance") not in allowed_values:
        raise BadRequest(description=msg)

    if data.get("urgency") and data.get("urgency") not in allowed_values:
        raise BadRequest(description=msg)




def serialize_task(task):
    return {
        "id":task[0][0],
        "name":task[0][1],
        "description":task[0][2],
        "duration":task[0][3],
        "importance":task[0][4],
        "urgency":task[0][5]   
    }