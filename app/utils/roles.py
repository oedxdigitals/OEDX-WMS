from functools import wraps

from flask import (
    session,
    abort,
)


def roles_required(*roles):

    def decorator(view):

        @wraps(view)
        def wrapped(*args, **kwargs):

            if "user_id" not in session:
                abort(401)

            if session.get("role") not in roles:
                abort(403)

            return view(*args, **kwargs)

        return wrapped

    return decorator
