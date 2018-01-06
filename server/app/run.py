# module
from flask import Flask, jsonify, request, Response
from flask_restful import Resource, Api, reqparse
from datetime import datetime, timedelta
import time
import json as json_obj
from cassandra.cqlengine import connection
from utils import to_dict, before_write
# file
import config
from config import db_keyspace, db_host, debug, app_host, app_port
import store

# connect databse
try:
    connection.setup([db_host], db_keyspace, lazy_connect=True)
    print("Make connection to DB")
except Exception as e:
    print("Error: connection db failed")
    raise

app = Flask(__name__, static_url_path='/static')
# inject config to app
configNames = [item for item in dir(config) if not item.startswith("__")]
for name in configNames:
    app.config[name] = config.__dict__[name]
app.config['MAX_CONTENT_LENGTH'] = app.config['request_maxContentLength']
# store app to store
store.app = app
import routes

if __name__ == '__main__':
    app.run(host=app_host,port=app_port, debug=debug, threaded=True)
