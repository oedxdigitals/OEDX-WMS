from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
)

from werkzeug.security import generate_password_hash

from app.extensions import db
from app.models.user import User
from app.forms.user import UserForm

from app.utils.auth import login_required
from app.utils.roles import roles_required


users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users",
)


@users_bp.route("/")
@login_required
@roles_required("Admin")
def index():

    users = User.query.order_by(
        User.username
    ).all()

    return render_template(
        "users/list.html",
        users=users,
    )


@users_bp.route("/new", methods=["GET", "POST"])
@login_required
@roles_required("Admin")
def new():

    form = UserForm()

    if form.validate_on_submit():

        exists = User.query.filter_by(
            username=form.username.data
        ).first()

        if exists:

            flash(
                "Username already exists.",
                "danger",
            )

            return render_template(
                "users/form.html",
                form=form,
            )

        user = User(

            username=form.username.data,

            password=generate_password_hash(
                form.password.data
            ),

            fullname=form.fullname.data,

            role=form.role.data,

            is_active=form.is_active.data,

        )

        db.session.add(user)

        db.session.commit()

        flash(
            "User created successfully.",
            "success",
        )

        return redirect(
            url_for("users.index")
        )

    return render_template(
        "users/form.html",
        form=form,
    )


@users_bp.route("/toggle/<int:user_id>")
@login_required
@roles_required("Admin")
def toggle(user_id):

    user = User.query.get_or_404(user_id)

    if user.username == "admin":

        flash(
            "Default admin cannot be disabled.",
            "warning",
        )

        return redirect(
            url_for("users.index")
        )

    user.is_active = not user.is_active

    db.session.commit()

    flash(
        "User updated.",
        "success",
    )

    return redirect(
        url_for("users.index")
    )
