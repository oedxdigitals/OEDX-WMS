from app.blueprints.dashboard import dashboard_bp
from app.blueprints.products import products_bp
from app.blueprints.suppliers import suppliers_bp
from app.blueprints.customers import customers_bp
from app.blueprints.goods_in import goods_in_bp
from app.blueprints.inventory import inventory_bp
from app.blueprints.goods_out import goods_out_bp
from app.blueprints.stock import stock_bp
from app.blueprints.reports import reports_bp
from app.blueprints.settings import settings_bp
from app.blueprints.report import report_bp
from app.blueprints.auth import auth_bp
from app.blueprints.users import users_bp
from app.blueprints.audit import audit_bp


def register_routes(app):

    app.register_blueprint(dashboard_bp)

    app.register_blueprint(products_bp)

    app.register_blueprint(suppliers_bp)

    app.register_blueprint(customers_bp)

    app.register_blueprint(goods_in_bp)

    app.register_blueprint(inventory_bp)

    app.register_blueprint(goods_out_bp)

    app.register_blueprint(stock_bp)

    app.register_blueprint(reports_bp)

    app.register_blueprint(settings_bp)

    app.register_blueprint(report_bp)

    app.register_blueprint(auth_bp)

    app.register_blueprint(users_bp)

    app.register_blueprint(audit_bp)
