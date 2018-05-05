# module
from flask import Flask
from cassandra.cqlengine import connection
import sys
import argparse
# from flask_session import Session
# file
import config
from config import db_keyspace, db_host, app_debug, app_host, app_port
from models import user
from plugins.auth import init_login_manager

# connect databse
try:
    connection.setup([db_host], db_keyspace, lazy_connect=True)
    print("Make connection to DB lazily")
except Exception as e:
    print("Error: connection db failed")
    raise

# init app
app = Flask(__name__, static_url_path='/static')
# inject config to app
configNames = [item for item in dir(config) if not item.startswith("__")]
for name in configNames:
    app.config[name] = config.__dict__[name]
app.config['MAX_CONTENT_LENGTH'] = app.config['request_maxContentLength']

# session is inited within it
init_login_manager(app, user)

# register routes
with app.app_context():
    from routes import routes
    from middlewares import globalMiddlewares
    from plugins.route import registerMany
    registerMany(routes, globalMiddlewares, app)

# bootstrap app
with app.app_context():
    if __name__ == '__main__':
        if len(sys.argv) == 1:
            app.run(host=app_host,port=app_port, debug=app_debug, threaded=True)
        else:
            parser = argparse.ArgumentParser()
            # when arg is default, user not input the arg
            DEFAULT_ARG = 'DEFAULT_ARG'
            parser.add_argument('--remigrate', nargs='?', default=DEFAULT_ARG)
            parser.add_argument('--seed', nargs='?', default=DEFAULT_ARG)
            args = parser.parse_args()
            # remigrate
            if args.remigrate != DEFAULT_ARG:
                import plugins.remigrate
            # load seeder
            if args.seed != DEFAULT_ARG:
                from plugins.seeder import execute
                execute('seeds.%s'%(args.seed or 'index'))