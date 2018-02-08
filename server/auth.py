from flask_login import LoginManager, login_user, logout_user, UserMixin
from flask import current_app as app, jsonify

app.secret_key = '\xfe\xfc\x8a\xebq>\xd4\x88\xa6\xccvkN,\xb89\xa9\xd97\xba\xb3R\x08\x1d'
class User(UserMixin):
    id = None
    email = None
    password = None

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return {'name': 'test'}

@app.route(app.config['api_prefix'] + "/login", methods=["GET"])
def login():
    # login and validate the user...
    a = User()
    a.id = 1
    a.email = 'asfas@asfa'
    login_user(a)
    return jsonify({'aaa': '123'})
