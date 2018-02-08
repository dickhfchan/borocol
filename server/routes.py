# module
from flask_restful import Api
from flask_cors import CORS
from flask import current_app as app, render_template
import json
# file
from controllers import ResourceController, QueryController, FileController, CourseDetailController
from utils import file_get_contents
import auth

# cors
CORS(app, resources={r"/api/*": {"origins": "*"}})

# spa
def renderSpa(fp):
    html = render_template(fp)
    initialData = {'serverRoot': '', 'clientBase': '/'} # serverRoot cant end with /
    html = html.replace('<head>', '<head><script>var initialData = %s;</script>'%(json.dumps(initialData)))
    return html
@app.route('/')
def index():
    return renderSpa('index.html')
@app.route('/<t1>')
@app.route('/<t1>/')
@app.route('/<t1>/<t2>')
@app.route('/<t1>/<t2>/')
def userAdmin(t1 = None, t2 = None):
    return renderSpa('spa.html')
# def aaa():
#     return '12412513'
# app.route(aaa,'/aaa')
# api
api = Api(app, prefix=app.config['api_prefix'])
api.add_resource(ResourceController, '/<string:model_name>', '/<string:model_name>/<string:id>')
api.add_resource(QueryController, '/<string:model_name>/query')
api.add_resource(FileController, '/file', '/file/<string:year>/<string:month>/<string:date>/<string:filename>')

api.add_resource(CourseDetailController, '/course_detail', '/course_detail/<string:model_name>/<string:id>')
