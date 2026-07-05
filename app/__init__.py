from flask import Flask

from config import Config

from app.extensions import db, migrate


def create_app():

    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent.parent

    flask_app = Flask(
        __name__,
        template_folder=str(BASE_DIR / "templates"),
        static_folder=str(BASE_DIR / "static"),
    )

    flask_app.config.from_object(Config)

    flask_app.secret_key = "oedx-wms-secret-key-change-me"

    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    import app.models

    from app.routes import register_routes
    register_routes(flask_app)

    from app.setup import create_default_admin

    with flask_app.app_context():

        db.create_all()

        create_default_admin()

    return flask_app
