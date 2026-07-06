from flask import Blueprint, render_template
from app.utils.auth import login_required
from app.utils.roles import roles_required

settings_bp = Blueprint(
    "settings",
    __name__,
    url_prefix="/settings"
)


@settings_bp.route("/")
@login_required
@roles_required("Admin")

def index():

    return render_template(
        "settings/index.html"
    )
