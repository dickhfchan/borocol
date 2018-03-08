from flask import current_app as app, request, render_template
import json
from flask_login import current_user
from utils import render_spa

class IndexController(object):
    def index(self):
        return render_spa('index.html')
    def partner_with_us(self):
        return render_spa('partner-with-us.html')
    def active_email(self):
        return render_spa('spa.html')
    def spa(self, t1 = None, t2 = None):
        return render_spa('spa.html')
