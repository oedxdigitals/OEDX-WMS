from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    url_for,
    flash,
    session,
)

from werkzeug.security import (
    check_password_hash,
)

from app.models.user import User

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"].strip()

        password = request.form["password"]

        user = User.query.filter_by(
            username=username
        ).first()

        if (
            user
            and user.is_active
            and check_password_hash(
                user.password,
                password
            )
        ):

            session["user_id"] = user.id
            session["username"] = user.username
            session["fullname"] = user.fullname
            session["role"] = user.role

            return redirect(url_for("dashboard.index"))

        flash(
            "Invalid username or password.",
            "danger"
        )

    return render_template(
        "auth/login.html"
    )


@auth_bp.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("auth.login")
    )
