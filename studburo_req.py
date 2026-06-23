from functools import wraps
from flask import current_app, abort
from flask import request
from flask import session
from flask_login import current_user
from csv_upload import dbcon
from flask_login import login_required

EXEMPT_METHODS = {"OPTIONS"}

def studienburo_required(func):

    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in EXEMPT_METHODS or current_app.config.get("LOGIN_DISABLED"):
            pass
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        else:
            user_id = current_user.get_id()
            with dbcon as connection:
                c = connection.cursor()
                c.execute("SELECT 1 FROM studienbüro_ma WHERE ma_id = ?", (user_id,))
                user_ist_studienburo = c.fetchone()

        if not user_ist_studienburo:
            abort(403)

        # nicht anfassen übernommen von login_required!!!!!!
        # flask 1.x compatibility
        # current_app.ensure_sync is only available in Flask >= 2.0
        if callable(getattr(current_app, "ensure_sync", None)):
            return current_app.ensure_sync(func)(*args, **kwargs)
        return func(*args, **kwargs)

    return decorated_view
