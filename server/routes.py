from flask import current_app as app
import controllers
from middlewares import auth
from plugins.route import group

def restful(names):
    return [{'path': '/' + v.replace('_', '-'), 'action': v, 'methods': ['POST']} for v in names]

#
routes = [
    *group({'controller': controllers.IndexController}, [
        {'path': '/', 'action': 'index', 'name': 'index'},
        {'path': app.config['api_prefix'] + '/initial-data', 'action': 'initial_data'},
        {'path': '/<t1>', 'action': 'index'},
        {'path': '/<t1>/<t2>', 'action': 'index'},
    ]),
    *group({'prefix': app.config['api_prefix']}, [
        # auth
        *group({'controller': controllers.UserController, 'prefix': '/user'}, [
            *restful(['current_user', 'register', 'login']),
            *group({'middlewares': [auth]}, [
                *restful(['logout', 'confirm_email', 'send_confirmation_email', 'update_email'])
            ]),
            # reset password
            *restful(['send_reset_password_email', 'check_reset_password_token', 'reset_password']),
        ]),
        # openid sign in and up
        *group({'prefix': '/google', 'controller': controllers.GoogleAuthController}, restful(['login', 'link', 'register'])),
        # file
        *group({'controller': controllers.FileController, 'prefix': '/file'}, [
            *restful(['store']),
            {'name': 'getFile', 'path': '/<year>/<month>/<date>/<filename>', 'action': 'get_file', 'methods': ['GET']},
        ]),
        # user
        *group({'controller': controllers.UserController, 'prefix': '/user', 'middlewares': [auth]}, [
            *restful(['profile']),
        ]),
        *group({'middlewares': [auth]}, [
            *group({'controller': controllers.CourseController, 'prefix': '/course'}, restful(['select', 'store', 'update', 'destroy'])),
        ]),
    ]),
]
