from flask import current_app as app
import controllers
from middlewares import auth
from plugins.route import group, generate

#
routes = [
    {'path': '/', 'controller': controllers.IndexController, 'action': 'index'},
    {'path': '/partner-with-us', 'controller': controllers.IndexController, 'action': 'partner_with_us'},
    {'path': '/active-email', 'name': 'activeEmail', 'controller': controllers.IndexController, 'action': 'active_email'},
    {'path': '/reset-password', 'name': 'resetPassword', 'controller': controllers.IndexController, 'action': 'reset_password'},
    {'path': '/<t1>', 'controller': controllers.IndexController, 'action': 'spa'},
    {'path': '/<t1>/<t2>', 'controller': controllers.IndexController, 'action': 'spa'},
    *group({'prefix': app.config['api_prefix']}, [
        *generate(controllers.CourseDetailController, '/course_detail'),
        *generate(controllers.UserController, '/user', [
            {'path': '/current_user', 'action': 'current_user', 'methods': ['GET']},
            {'path': '/register', 'action': 'register', 'methods': ['POST']},
            {'path': '/login', 'action': 'login', 'methods': ['POST']},
            *group({'middlewares': [auth]}, [
                {'path': '/logout', 'action': 'logout', 'methods': ['GET']},
                {'path': '/active-email', 'action': 'active_email', 'methods': ['POST']},
                {'path': '/send-activation-email', 'action': 'send_activation_email', 'methods': ['POST']},
                {'path': '/update-email', 'action': 'update_email', 'methods': ['POST']},
            ]),
            {'path': '/send-reset-password-email', 'action': 'send_reset_password_email', 'methods': ['POST']},
            {'path': '/check-reset-password-token', 'action': 'check_reset_password_token', 'methods': ['POST']},
            {'path': '/reset-password', 'action': 'reset_password', 'methods': ['POST']},
        ], True),
    ]),
]
