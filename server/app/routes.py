# module
from flask_restful import Api
from flask_cors import CORS
# file
from controllers import ResourceController, QueryController, FileController
from store import app

# cors
CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app, prefix='/api/v1')
api.add_resource(ResourceController, '/<string:model_name>', '/<string:model_name>/<string:id>')
api.add_resource(QueryController, '/<string:model_name>/query')
api.add_resource(FileController, '/file', '/file/<string:filename>', endpoint = 'uploaded_file')
