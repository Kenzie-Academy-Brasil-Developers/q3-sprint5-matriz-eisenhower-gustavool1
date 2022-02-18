from app.routes.categories_blueprint import bp as bp_cateogories
from app.routes.tasks_blueprint import bp as bp_tasks
def init_app(app):
    app.register_blueprint(bp_cateogories)
    app.register_blueprint(bp_tasks)