from config import keyspace, host, debug, api_port
from flask import Flask, jsonify, request, Response
from flask_restful import Resource, Api, reqparse
from datetime import datetime, timedelta
import pandas as pd
import time
import json as json_obj
from flask_restful.utils import cors
from cassandra.cqlengine import connection
from utils import toDict
# db
import models

connection.setup([host], keyspace)

app = Flask(__name__)
api = Api(app)

#print "Make connection to DB"
#print conn

default_headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods':'GET,POST,PUT,PATCH,DELETE,OPTIONS',
    'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Connection, User-Agent, Cookie'
    }

#Create datatime columns

# dt_columns = ['create_ts','start_date', 'end_date', 'update_ts', 'last_loc_update_ts', 'apps_ts', 'last_access_ts', 'last_login_ts']
dt_columns = []

class ResourceHandler(Resource):
    def get(self,model_name, id=None):
        if id:
            return {'resource': toDict(models.__dict__[model_name].objects.filter(id=id).first())}, 200, default_headers
        else:
            page = int(request.args.get('page') or 1)
            per_page = int(request.args.get('perPage') or 20)
            start = (page - 1) * per_page
            end = page * per_page

            return {'resources': {'userType': None, 'email': None, 'password': u'123', 'id': u'1', 'privacy': None}}, 200, default_headers
            return {'resources': toDict(models.__dict__[model_name].objects.all()[start:end])}, 200, default_headers
    # Handle POST event for an insertion/Update event:
    # User must set "Content-Type" to "application/json" in POST request
    # Use table attributes given in MySQL schema for JSON keys
    @cors.crossdomain(origin='*')
    def post(self, model_name, id=None):
        pass
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
