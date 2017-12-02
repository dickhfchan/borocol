from config import keyspace, host, debug, api_port
from flask import Flask, jsonify, request, Response
from flask_restful import Resource, Api, reqparse
from datetime import datetime, timedelta
import time
import json as json_obj
from flask_restful.utils import cors
from cassandra.cqlengine import connection
from utils import to_dict, before_write
# db
import models

try:
    connection.setup([host], keyspace)
except Exception as e:
    print "Error: connection db failed"
    raise

app = Flask(__name__)
api = Api(app)

#print "Make connection to DB"
#print conn

default_headers = {
    'Content-type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods':'GET,POST,PUT,PATCH,DELETE,OPTIONS',
    'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Connection, User-Agent, Cookie'
    }

#Create datatime columns

# dt_columns = ['create_ts','start_date', 'end_date', 'update_ts', 'last_loc_update_ts', 'apps_ts', 'last_access_ts', 'last_login_ts']
dt_columns = []

class ResourceHandler(Resource):
    def get(self,model_name, id=None):
        model = models.__dict__[model_name]
        if id:
            return {'resource': to_dict(model.objects.filter(id=id).first())}, 200, default_headers
        else:
            page = int(request.args.get('page') or 1)
            per_page = int(request.args.get('perPage') or 20)
            start = (page - 1) * per_page
            end = page * per_page
            return {'resources': to_dict(model.objects.all()[start:end])}, 200, default_headers
    # Handle POST event for an insertion/Update event:
    # User must set "Content-Type" to "application/json" in POST request
    # Use table attributes given in MySQL schema for JSON keys
    def post(self, model_name, id=None):
        model = models.__dict__[model_name]
        # make data
        data = {}
        for key in request.form:
            data[key] = request.form[key]
        before_write(data, model)
        data['created_at'] = data['updated_at'] = datetime.now()
        data['id'] = id or request.form['id']
        # check exits
        errorMsg = None
        item = model.objects(id = data['id']).first()
        if item:
            errorMsg = 'Item already exists'
        else:
            # write
            try:
                model.create(**data)
            except Exception as e:
                errorMsg = e.message
        return {'result': 'failed' if errorMsg else 'success', 'message': errorMsg}, 200, default_headers

    def put(self, model_name, id=None):
        model = models.__dict__[model_name]
        # make data
        data = {}
        for key in request.form:
            data[key] = request.form[key]
        before_write(data, model)
        data['updated_at'] = datetime.now()
        # write
        errorMsg = None
        try:
            model.objects(id=id).if_exists().update(**data)
        except Exception as e:
            errorMsg = e.message
        return {'result': 'failed' if errorMsg else 'success', 'message': errorMsg}, 200, default_headers
    def delete(self, model_name, id=None):
        model = models.__dict__[model_name]
        ids = [id] if ',' not in id else id.split(',')
        try:
            model.objects.filter(id__in=ids).if_exists().delete()
        except Exception as e:
            errorMsg = e.message
        return {'result': 'failed' if errorMsg else 'success', 'message': errorMsg}, 200, default_headers

    def options(self, model_name, id=None):
        print default_headers
        return '', 200, default_headers
class QueryHandler(Resource):
    pass

@app.route('/')
def index():
    return "Hello_World"

api.add_resource(ResourceHandler, *[
    '/api/<string:model_name>',
    '/api/<string:model_name>/<string:id>'
])
api.add_resource(QueryHandler, *[
    '/api/<string:model_name>/query',
])

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=api_port, debug=debug, threaded=True)
