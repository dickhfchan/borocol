from config import keyspace, host, debug, api_port
from flask import Flask, jsonify, request, Response

app = Flask(__name__)

#print "Make connection to DB"
#print conn

default_headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods':'GET,POST,PUT,PATCH,DELETE,OPTIONS',
    'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, Connection, User-Agent, Cookie'
    }

@app.route('/')
def index():
    print int(request.args.get('page')or 1)
    return "Hello_World"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=api_port, debug=debug, threaded=True)
