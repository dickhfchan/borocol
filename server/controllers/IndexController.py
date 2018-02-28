from flask import current_app as app, request, render_template
import json
from UserController import UserController
from flask_login import current_user

class IndexController(object):
    def _renderSpa(self, fp):
        html = render_template(fp)
        initialData = {'serverRoot': '', 'clientBase': '/'} # serverRoot cant end with /
        initialData['recaptcha'] = {'sitekey': app.config['recaptcha_sitekey']}
        # inject user info
        if current_user.is_authenticated:
            c = UserController()
            initialData['authenticated'] = True
            initialData['user'] = c.get_user_dict(current_user)
        #
        html = html.replace('<head>', '<head><script>var initialData = %s;</script>'%(json.dumps(initialData)))
        return html
    def index(self):
        return self._renderSpa('index.html')
    def partnerWithUs(self):
        return self._renderSpa('partner-with-us.html')
    def spa(self, t1 = None, t2 = None):
        return self._renderSpa('spa.html')
