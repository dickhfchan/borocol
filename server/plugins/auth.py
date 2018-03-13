from flask_login import LoginManager

# session is inited within it
def init_login_manager(app, userModel):
    app.secret_key = app.config['app_key']
    login_manager = LoginManager()
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(userid):
        return userModel.objects(id=userid).first()
