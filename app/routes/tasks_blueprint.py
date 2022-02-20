from flask import Blueprint

from app.controllers.tasks_controller import create_task, delete_task, update_task

bp = Blueprint("bp_tasks", __name__)

bp.post("/tasks")(create_task)
bp.patch("/tasks/<int:id>")(update_task)
bp.delete("/tasks/<int:id>")(delete_task)