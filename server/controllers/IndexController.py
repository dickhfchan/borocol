from flask import current_app as app, request, render_template
import json

class IndexController(object):
    def _renderSpa(self, fp):
        html = render_template(fp)
        initialData = {'serverRoot': '', 'clientBase': '/'} # serverRoot cant end with /
        html = html.replace('<head>', '<head><script>var initialData = %s;</script>'%(json.dumps(initialData)))
        return html
    def index(self):
        return self._renderSpa('index.html')
    def spa(self, t1 = None, t2 = None):
        return self._renderSpa('spa.html')
