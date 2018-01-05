# module
from flask import Flask, jsonify, request, Response
from flask_restful import Resource, Api, reqparse
from datetime import datetime, timedelta
import time
import json as json_obj
from cassandra.cqlengine import connection
from utils import to_dict, before_write
# file
from config import keyspace, db_host, debug, app_host, app_port
import store

# connect databse
try:
    connection.setup([db_host], keyspace, lazy_connect=True)
    print("Make connection to DB")
except Exception as e:
    print("Error: connection db failed")
    raise

app = Flask(__name__)
store.app = app
import routes

if __name__ == '__main__':
    app.run(host=app_host,port=app_port, debug=debug, threaded=True)
