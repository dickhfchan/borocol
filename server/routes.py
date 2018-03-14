from flask import current_app as app
import controllers
from middlewares import auth
from plugins.route import group

def restful(names):
    return [{'path': '/' + v.replace('_', '-'), 'action': v, 'methods': ['POST']} for v in names]

#
routes = [
    *group({'controller': controllers.IndexController}, [
        {'path': '/', 'action': 'index'},
        {'path': '/partner-with-us', 'action': 'partner_with_us'},
        {'path': '/active-email', 'name': 'activeEmail', 'action': 'active_email'},
        {'path': '/reset-password', 'name': 'resetPassword', 'action': 'reset_password'},
        {'path': '/<t1>', 'action': 'spa'},
        {'path': '/<t1>/<t2>', 'action': 'spa'},
    ]),
    *group({'prefix': app.config['api_prefix']}, [
        # auth
        *group({'controller': controllers.UserController, 'prefix': '/user'}, [
            *restful(['current_user', 'register', 'login']),
            *group({'middlewares': [auth]}, [
                *restful(['logout', 'active_email', 'send_activation_email', 'update_email'])
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
        #
        *group({'middlewares': [auth]}, [
            *group({'controller': controllers.CourseController, 'prefix': '/course'}, restful(['select', 'store', 'update', 'destroy'])),
        ]),
    ]),
]
