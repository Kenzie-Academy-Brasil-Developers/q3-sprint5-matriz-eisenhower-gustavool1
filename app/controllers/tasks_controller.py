from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.tasks_model import TasksModel
from app.services.task_services import checking_repeated_categories, finding_classfication, creating_category, validating_body, creating_tasks_categories
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation


def create_task():
    try:
        data = dict(request.get_json())
        session = current_app.db.session
        categorys_ids = []
        if validating_body(data["importance"], data["urgency"]):
            return validating_body(data["importance"], data["urgency"]), HTTPStatus.BAD_REQUEST

        if data.get("categories"):
            non_repeated_categories = checking_repeated_categories(data["categories"])
            created_categorys = creating_category(non_repeated_categories)
            categorys_ids = [category.id for category in created_categorys if category.id ]
            categories = data.pop("categories", None)


        classification = finding_classfication(data["importance"], data["urgency"])
        data["eisenhower_id"] = classification.id
        task = TasksModel(**data)
        
        session.add(task)
        session.commit()
        
        if categorys_ids:
            creating_tasks_categories(categorys_ids, task.id)
        
        return {
            "id":task.id,
            "name":task.name,
            "description":task.description,
            "duration":task.duration,
            "classification":classification.type,
            "categories":categories
        }, HTTPStatus.CREATED
    
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation ):
            return {"msg": "task already exists!"}, HTTPStatus.CONFLICT
