from flask import (
    request,
    session,
)

from app.extensions import db
from app.models.audit_log import AuditLog


def log_action(
    action,
    module,
    description,
):

    log = AuditLog(

        user_id=session.get("user_id"),

        username=session.get("username"),

        action=action,

        module=module,

        description=description,

        ip_address=request.remote_addr,

    )

    db.session.add(log)

    db.session.commit()
