from flask import current_app as app
import json
from flask_login import current_user
from utils import success, failed

# global middlewares
def actionHandler(next, *args, **kwargs):
    response = next()
    # complete response
    if not isinstance(response, tuple):
        response = (response, 200, {})
    else:
        if len(response) == 1:
            response = response + (200, {})
        elif len(response) == 2:
            response = response + ({},)
    # convert data to json if possible
    data = response[0]
    if isinstance(data, list) or isinstance(data, dict):
        response = list(response)
        response[0] = json.dumps(data)
        headers = response[2]
        headers['Content-Type'] = 'application/json'
        response = tuple(response)
    return response

globalMiddlewares = [actionHandler]

# others
# auth
def auth(next, *args, **kwargs):
    if not current_user.is_authenticated:
        return failed('Unauthorized',code = 401)
    return next()
