from views.auth_views import auth_bp

def register_bp(app):
    app.register_blueprint(auth_bp)
