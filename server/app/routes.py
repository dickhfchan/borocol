# module
from flask_restful import Api
from flask_restful.utils.cors import crossdomain
# file
from controllers import ResourceController, QueryController
from store import app

# todo replace cros with flask_restful.utils.cors.crossdomain
api = Api(app, prefix='/api/v1', decorators=[crossdomain(origin='*')])
api.add_resource(ResourceController, *[
    '/<string:model_name>',
    '/<string:model_name>/<string:id>'
])
api.add_resource(QueryController, *[
    '/<string:model_name>/query',
])
