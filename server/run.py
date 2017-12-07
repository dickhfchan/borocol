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

# connect databse
try:
    connection.setup([host], keyspace)
except Exception as e:
    print("Error: connection db failed")
    raise

# init app, api
app = Flask(__name__)
api = Api(app)

#print("Make connection to DB")
#print(conn)

# cros header
default_headers = {
    'Content-type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods':'GET,POST,PUT,PATCH,DELETE,OPTIONS',
    'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Connection, User-Agent, Cookie'
    }

#Create datatime columns

# for get ,save and delete data
class ResourceHandler(Resource):
    # get data
    def get(self,model_name, id=None):
        # model class
        model = models.__dict__[model_name]
        if id:
            # return one row
            return {'resource': to_dict(model.objects.filter(id=id).first())}, 200, default_headers
        else:
            # return resources list
            # default page: 1, per_page: 20
            page = int(request.args.get('page') or 1)
            per_page = int(request.args.get('per_page') or 20)
            start = (page - 1) * per_page
            end = page * per_page
            return {'resources': to_dict(model.objects.all()[start:end])}, 200, default_headers
    # create a row; will check row if exist by id
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
    # update a row
    def put(self, model_name, id=None):
        model = models.__dict__[model_name]
        # make data
        data = {}
        for key in request.form:
            data[key] = request.form[key]
        before_write(data, model)
        data['updated_at'] = datetime.now()
        del data['id'] # prevent change id
        # write
        errorMsg = None
        try:
            model.objects(id=id).if_exists().update(**data)
        except Exception as e:
            errorMsg = e.message
        return {'result': 'failed' if errorMsg else 'success', 'message': errorMsg}, 200, default_headers
    # delete a row or many rows
    def delete(self, model_name, id=None):
        model = models.__dict__[model_name]
        ids = [id] if ',' not in id else id.split(',')
        try:
            model.objects.filter(id__in=ids).if_exists().delete()
        except Exception as e:
            errorMsg = e.message
        return {'result': 'failed' if errorMsg else 'success', 'message': errorMsg}, 200, default_headers
    # for cros non-get requests
    def options(self, model_name, id=None):
        print(default_headers)
        return '', 200, default_headers

# todo: get data with conditions
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
