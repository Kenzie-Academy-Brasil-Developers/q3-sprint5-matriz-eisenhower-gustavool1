from app.routes.categories_blueprint import bp as bp_cateogories

def init_app(app):
    app.register_blueprint(bp_cateogories)