from flask_login import LoginManager, login_user, logout_user, UserMixin, login_required, current_user
from flask import current_app as app, jsonify
from flask.views import MethodView


app.secret_key = '\xfe\xfc\x8a\xebq>\xd4\x88\xa6\xccvkN,\xb89\xa9\xd97\xba\xb3R\x08\x1d'
class User(UserMixin):
    id = None
    email = None
    password = None

login_manager = LoginManager()
login_manager.init_app(app)

a = User()
a.id = 1
a.email = 'asfas@asfa'
@login_manager.user_loader
def load_user(userid):
    return a

@app.route(app.config['api_prefix'] + "/login", methods=["GET"])
def login():
    # login and validate the user...
    # logout_user()
    login_user(a)
    return jsonify({'aaa': '123'})

@app.route("/a", methods=["GET"])
# @login_required
def fname():
    return app.login_manager.unauthorized()
    print(current_user.is_anonymous)
    return jsonify(current_user.__dict__)

class UserAPI(MethodView):

    def get(self):
        return jsonify({'aaa': '123'})

    def post(self):
        return

app.add_url_rule('/b', view_func=UserAPI.as_view('users'))
