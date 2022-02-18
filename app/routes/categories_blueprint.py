from flask import Blueprint
from app.controllers.categories_controller import create_categorie, delete_categorie, update_categorie


bp = Blueprint("categories_blueprint", __name__)

bp.post("/categories")(create_categorie)
bp.patch("/categories/<int:id>")(update_categorie)
bp.delete("/categories/<int:id>")(delete_categorie)
