import string
from flask import request, current_app, jsonify
from app.models.categories_model import CategoriesModel
from http import HTTPStatus
from werkzeug.exceptions import NotFound
def updating_categories(categories, update):
    session = current_app.db.session

    for index,categorie_to_update  in enumerate(update):
        categorie = CategoriesModel.query.filter(CategoriesModel.id ==  categories[index].category_id).first()
        
        if type(update[index]) is str:
            categorie.name = update[index]
            session.add(categorie)

        if type(update[index]) is dict:
            for key,value in update[index].items():
                setattr(categorie, key, value)
                session.add(categorie)
            
    session.commit()
 

def serialize_categorie(categorie):
    return {
        "id":categorie.id,
        "name":categorie.name,
        "description":categorie.description,
    }