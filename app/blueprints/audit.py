from flask import Blueprint, render_template

from app.models.audit_log import AuditLog

from app.utils.auth import login_required
from app.utils.roles import roles_required


audit_bp = Blueprint(
    "audit",
    __name__,
    url_prefix="/audit",
)


@audit_bp.route("/")
@login_required
@roles_required("Admin")
def index():

    logs = AuditLog.query.order_by(
        AuditLog.created_at.desc()
    ).all()

    return render_template(
        "audit/list.html",
        logs=logs,
    )
