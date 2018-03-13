from flask import current_app as app
import controllers
from middlewares import auth
from plugins.route import group

def restful(names):
    return [{'path': '/' + v, 'action': v, 'methods': ['POST']} for v in names]

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
            {'path': '/current_user', 'action': 'current_user', 'methods': ['GET']},
            {'path': '/register', 'action': 'register', 'methods': ['POST']},
            {'path': '/login', 'action': 'login', 'methods': ['POST']},
            *group({'middlewares': [auth]}, [
                {'path': '/logout', 'action': 'logout', 'methods': ['GET']},
                {'path': '/active-email', 'action': 'active_email', 'methods': ['POST']},
                {'path': '/send-activation-email', 'action': 'send_activation_email', 'methods': ['POST']},
                {'path': '/update-email', 'action': 'update_email', 'methods': ['POST']},
            ]),
            # reset password
            {'path': '/send-reset-password-email', 'action': 'send_reset_password_email', 'methods': ['POST']},
            {'path': '/check-reset-password-token', 'action': 'check_reset_password_token', 'methods': ['POST']},
            {'path': '/reset-password', 'action': 'reset_password', 'methods': ['POST']},
        ]),
        # openid sign in and up
        *group({'prefix': '/google', 'controller': controllers.GoogleAuthController}, [
            {'path': '/login', 'action': 'login', 'methods': ['POST']},
            {'path': '/link', 'action': 'link', 'methods': ['POST']},
        ]),
        *group({'middlewares': [auth]}, [
            *group({'controller': controllers.CourseController, 'prefix': '/course'}, restful(['select', 'store', 'update', 'destroy'])),
        ]),
    ]),
]
