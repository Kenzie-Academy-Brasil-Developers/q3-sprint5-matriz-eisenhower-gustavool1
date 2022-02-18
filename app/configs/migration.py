from flask_migrate import Migrate

def init_app(app):
    from app.models.tasks_categories_model import TaskCategoriesModel
    from app.models.tasks_model import TasksModel
    from app.models.eisenhowers_model import EisenhowersModel
    from app.models.categories_model import CategoriesModel    
    Migrate(app, app.db)
    