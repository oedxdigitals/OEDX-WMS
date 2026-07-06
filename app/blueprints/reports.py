from flask import Blueprint, render_template
from app.utils.auth import login_required
from app.utils.roles import roles_required

reports_bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/reports"
)


@reports_bp.route("/")
@login_required
@roles_required(
    "Admin",
    "Supervisor",
)
def index():

    return render_template(
        "reports/index.html"
    )
