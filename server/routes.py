# module
from flask_restful import Api
from flask_cors import CORS
from flask import current_app as app
import json
# file
from controllers import ResourceController, QueryController, FileController
from utils import file_get_contents

# cors
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
@app.route('/<t1>')
@app.route('/<t1>/<t2>')
def index():
    html = file_get_contents('./static/index.html')
    initialData = {'serverRoot': '', 'clientBase': '/'} # serverRoot cant end with /
    html = html.replace('<head>', '<head><script>var initialData = %s;</script>'%(json.dumps(initialData)))
    return html

api = Api(app, prefix='/api/v1')
api.add_resource(ResourceController, '/<string:model_name>', '/<string:model_name>/<string:id>')
api.add_resource(QueryController, '/<string:model_name>/query')
api.add_resource(FileController, '/file', '/file/<string:year>/<string:month>/<string:date>/<string:filename>')
