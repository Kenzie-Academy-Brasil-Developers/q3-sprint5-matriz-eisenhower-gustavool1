from http import HTTPStatus
from flask import current_app, jsonify, request, session
from app.models.tasks_categories_model import TaskCategoriesModel
from app.models.categories_model import CategoriesModel
from app.models.tasks_model import TasksModel
from app.services.task_services import checking_repeated_categories, finding_classfication, creating_category, validating_body, creating_tasks_categories, validating_update
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation
from werkzeug.exceptions import BadRequest
from app.services.categories_services import updating_categories


def create_task():
    try:
        data = dict(request.get_json())
        session = current_app.db.session
        categorys_ids = []

        validating_body(data["importance"], data["urgency"])

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

    except BadRequest as e:
        return e.description, e.code



def update_task(id):
    try:
        data = request.get_json()
        session = current_app.db.session
        task = TasksModel.query.filter(TasksModel.id == id).first()
        validating_update(data)

        if not task:
            return { "msg": "task not found!"}, HTTPStatus.NOT_FOUND
        
        for key, value in data.items():
            if key != 'categories':
                setattr(task, key, value)

        

        session.add(task)
        session.commit()
        classification = finding_classfication(task.importance, task.urgency)
        tasks_categories_id = TaskCategoriesModel.query.filter(TaskCategoriesModel.task_id == id).order_by(TaskCategoriesModel.category_id).all()
        if data.get("categories"):
            updating_categories(tasks_categories_id, data["categories"] )
        categories = []
        

        for index, task_categorie in enumerate(tasks_categories_id):
            categorie = CategoriesModel.query.filter(CategoriesModel.id == task_categorie.category_id).first()
            categories.append(categorie.name)
        

        return {
            "id":task.id,
            "name":task.name,
            "description":task.description,
            "duration":task.duration,
            "classification":classification.type,
            "categories":categories
        }, HTTPStatus.OK

    except BadRequest as e:
        return e.description, e.code

    




def delete_task(id):
    session = current_app.db.session
    task_delete = TasksModel.query.filter(TasksModel.id == id).first()

    if not task_delete:
        return {"msg": "task not found!"}, HTTPStatus.NOT_FOUND

    session.delete(task_delete)
    session.commit()
    return "", HTTPStatus.NO_CONTENT

