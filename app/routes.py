from app.blueprints.dashboard import dashboard_bp
from app.blueprints.products import products_bp
from app.blueprints.suppliers import suppliers_bp

def register_routes(app):
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(suppliers_bp)
