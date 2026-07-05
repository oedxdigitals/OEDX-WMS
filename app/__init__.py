from flask import Flask

from config import Config
from app.extensions import db, migrate

import os


def create_app():

    BASE_DIR = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )

    flask_app = Flask(
        __name__,
        template_folder=os.path.join(BASE_DIR, "templates"),
        static_folder=os.path.join(BASE_DIR, "static"),
    )

    flask_app.config.from_object(Config)

    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    import app.models

    from app.routes import register_routes
    register_routes(flask_app)

    return flask_app
