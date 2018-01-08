# module
from flask_restful import Api
from flask_cors import CORS
from flask import current_app as app
# file
from controllers import ResourceController, QueryController, FileController

# cors
CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app, prefix='/api/v1')
api.add_resource(ResourceController, '/<string:model_name>', '/<string:model_name>/<string:id>')
api.add_resource(QueryController, '/<string:model_name>/query')
api.add_resource(FileController, '/file', '/file/<string:year>/<string:month>/<string:date>/<string:filename>')
