from flask import Blueprint

from app.controllers.before_first_request_controller import populating_db

bp = Blueprint("bp_before_first_request", __name__)

bp.before_app_first_request(populating_db)