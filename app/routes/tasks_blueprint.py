from flask import Blueprint

from app.controllers.tasks_controller import create_task

bp = Blueprint("bp_tasks", __name__)

bp.post("/tasks")(create_task)