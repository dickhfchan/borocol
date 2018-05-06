from flask import current_app as app, request, render_template
import json
from flask_login import current_user
from utils import failed, success, user_to_dict

class IndexController(object):
    def index(self, t1 = None, t2 = None):
        return render_template('index.html')
    def initial_data(self):
        initialData = {}
        initialData['recaptcha'] = {'sitekey': app.config['recaptcha_sitekey']}
        initialData['google_signin'] = {'client_id': app.config['google_singin_client_id']}
        initialData['site_name'] = app.config['site_name']
        initialData['site_home_title'] = app.config['site_home_title']
        # inject user info
        if current_user.is_authenticated:
            initialData['authenticated'] = True
            initialData['user'] = user_to_dict(current_user)
        return success(data=initialData)
