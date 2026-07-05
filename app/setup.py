from werkzeug.security import generate_password_hash

from app.extensions import db
from app.models.user import User


def create_default_admin():

    admin = User.query.filter_by(
        username="admin"
    ).first()

    if admin:
        return

    admin = User(
        username="admin",
        password=generate_password_hash("admin123"),
        fullname="System Administrator",
        role="Admin",
        is_active=True,
    )

    db.session.add(admin)
    db.session.commit()

    print("Default admin created")

