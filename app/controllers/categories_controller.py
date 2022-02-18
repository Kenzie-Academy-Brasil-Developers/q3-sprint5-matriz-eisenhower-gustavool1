from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.categories_model import CategoriesModel
from sqlalchemy.exc import IntegrityError

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