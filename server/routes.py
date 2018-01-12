# module
from flask_restful import Api
from flask_cors import CORS
from flask import current_app as app, render_template
import json
# file
from controllers import ResourceController, QueryController, FileController, CourseDetailController
from utils import file_get_contents

# cors
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/user-admin')
@app.route('/user-admin/<t1>')
@app.route('/user-admin/<t1>/')
@app.route('/user-admin/<t1>/<t2>')
def userAdmin(t1 = None, t2 = None):
    html = render_template('user-admin.html')
    initialData = {'serverRoot': '', 'clientBase': '/user-admin/'} # serverRoot cant end with /
    html = html.replace('<head>', '<head><script>var initialData = %s;</script>'%(json.dumps(initialData)))
    return html

api = Api(app, prefix='/api/v1')
api.add_resource(ResourceController, '/<string:model_name>', '/<string:model_name>/<string:id>')
api.add_resource(QueryController, '/<string:model_name>/query')
api.add_resource(FileController, '/file', '/file/<string:year>/<string:month>/<string:date>/<string:filename>')

api.add_resource(CourseDetailController, '/course_detail', '/course_detail/<string:model_name>/<string:id>')
