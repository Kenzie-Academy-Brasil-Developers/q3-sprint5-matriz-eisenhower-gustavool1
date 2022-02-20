from app.routes.categories_blueprint import bp as bp_cateogories
from app.routes.tasks_blueprint import bp as bp_tasks
from app.routes.before_first_request_blueprint import bp as bp_before_first_request
def init_app(app):
    app.register_blueprint(bp_cateogories)
    app.register_blueprint(bp_tasks)
    app.register_blueprint(bp_before_first_request)