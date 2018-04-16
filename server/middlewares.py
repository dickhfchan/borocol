from flask import current_app as app
from flask_login import current_user
from utils import success, failed
from plugins.middlewareHelper import actionHandler

# global middlewares
globalMiddlewares = [actionHandler]

# others
# auth
def auth(next, *args, **kwargs):
    if not current_user.is_authenticated:
        return failed('Unauthenticated',code = 401)
    return next()
