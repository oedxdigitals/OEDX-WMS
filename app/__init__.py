from flask import Flask

from config import Config
from app.extensions import db, migrate


def create_app():
    flask_app = Flask(__name__)

    flask_app.config.from_object(Config)

    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    import app.models

    from app.routes import register_routes
    register_routes(flask_app)

    return flask_app
