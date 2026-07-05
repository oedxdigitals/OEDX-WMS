from app.blueprints.dashboard import dashboard_bp
from app.blueprints.products import products_bp
from app.blueprints.suppliers import suppliers_bp
from app.blueprints.customers import customers_bp
from app.blueprints.goods_in import goods_in_bp
from app.blueprints.inventory import inventory_bp


def register_routes(app):

    app.register_blueprint(dashboard_bp)

    app.register_blueprint(products_bp)

    app.register_blueprint(suppliers_bp)

    app.register_blueprint(customers_bp)

    app.register_blueprint(goods_in_bp)

    app.register_blueprint(inventory_bp)
