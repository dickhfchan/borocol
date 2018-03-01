from flask import current_app as app
from flask_mail import Mail

mail = Mail(app)
