from .auth_view import auth_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
