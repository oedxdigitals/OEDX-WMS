from flask import Flask

from config import Config
from app.extensions import db
from app.routes import register_routes


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    register_routes(app)

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True,
    )
