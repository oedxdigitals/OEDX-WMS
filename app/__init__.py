from flask import Flask

from config import Config

from app.extensions import db
from app.extensions import migrate


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.routes import register_routes

    register_routes(app)

    with app.app_context():
        from app import models

    return app
