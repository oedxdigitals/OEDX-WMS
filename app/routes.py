from app.blueprints.dashboard import dashboard_bp


def register_routes(app):
    app.register_blueprint(dashboard_bp)
