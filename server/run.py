# module
from flask import Flask
from cassandra.cqlengine import connection
from flask_login import LoginManager
# file
import config
from config import db_keyspace, db_host, app_debug, app_host, app_port
from models import user

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

# init login_manager
app.secret_key = config.app_key
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(userid):
    return user.objects(id=userid).first()

# register routes
with app.app_context():
    from routes import routes
    from middlewares import globalMiddlewares
    from plugins.route import registerMany
    registerMany(routes, globalMiddlewares, app)

# bootstrap app
if __name__ == '__main__':
    app.run(host=app_host,port=app_port, debug=app_debug, threaded=True)
