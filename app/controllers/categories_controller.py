from http import HTTPStatus
from unicodedata import category, name
from flask import current_app, jsonify, request
from app.models.categories_model import CategoriesModel
from sqlalchemy.exc import IntegrityError

from app.models.tasks_categories_model import TaskCategoriesModel
from app.models.tasks_model import TasksModel
from app.services.categories_services import serialize_categorie
from app.services.task_services import serialize_task

def create_categorie():
    try:
        data = request.get_json()
        session = current_app.db.session
        
        categorie = CategoriesModel(**data)

        session.add(categorie)
        session.commit()

        return jsonify(categorie), HTTPStatus.CREATED

    except IntegrityError:
        return {"msg":"category already exists!"}, HTTPStatus.CONFLICT



def update_categorie(id):
    data = request.get_json()
    session = current_app.db.session

    categorie = CategoriesModel.query.filter(CategoriesModel.id == id).first()

    if not categorie:
        return {"msg": "category not found!"}, HTTPStatus.NOT_FOUND

    for key,value in data.items():
        if key != "id":
            setattr(categorie, key, value)

    session.add(categorie)
    session.commit()
    return jsonify(categorie), HTTPStatus.OK



def delete_categorie(id):
    session = current_app.db.session
    categorie_deleted = CategoriesModel.query.filter(CategoriesModel.id == id).first()

    if not categorie_deleted:
        return {"msg": "category not found!"}, HTTPStatus.NOT_FOUND
        

    session.delete(categorie_deleted)
    session.commit()

    
    return "", HTTPStatus.NO_CONTENT



def get_categories():

    session = current_app.db.session
    all_task_categories = TaskCategoriesModel.query.all()
    all_categories = []

    for task_categorie in all_task_categories:
        category = CategoriesModel.query.filter(CategoriesModel.id == task_categorie.category_id).first()
        category = serialize_categorie(category)

        task =  (session.query(
        TasksModel.id,
        TasksModel.name,
        TasksModel.description,
        TasksModel.duration,
        TasksModel.importance,
        TasksModel.urgency,
        
        )
        .select_from(TaskCategoriesModel)
        .join(CategoriesModel)
        .join(TasksModel)
        .filter(task_categorie.category_id == TaskCategoriesModel.category_id )
        .all()
        )
        task = serialize_task(task)
        category["tasks"] = []
        category["tasks"].append(task)
        all_categories.append(category)
    return jsonify(all_categories)