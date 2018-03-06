from os import path
# env
env = None
try:
    import env
except Exception as e:
    pass

# db
db_keyspace = "borocol"
db_host = '127.0.0.1'
# app
app_debug = getattr(env, 'debug', False)
app_host = '127.0.0.1' # dev
app_port = 8081 # dev
app_name = 'Borocol'
app_path = path.dirname(__file__)
app_key = '\xfe\xfc\x8a\xebq>\xd4\x88\xa6\xccvkN,\xb89\xa9\xd97\xba\xb3R\x08\x1d'
# api
api_prefix = '/api/v1'
# request
request_maxContentLength = 16 * 1024 * 1024 # 16m MAX_CONTENT_LENGTH
# file
file_uploadDir = path.join(app_path, 'uploads')
file_allowedExtensions = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'webp'])
# google recaptcha
recaptcha_sitekey = '6LdizkgUAAAAANJGphKgKtGcERgbagwAAL91kti4'
recaptcha_secretkey = '6LdizkgUAAAAAB_bXXnjnjWomYSTy4GxVn7umQnf'
# mail
# MAIL_SERVER : default ‘localhost’
# MAIL_PORT : default 25
# MAIL_USE_TLS : default False
# MAIL_USE_SSL : default False
# MAIL_DEBUG : default app.debug
# MAIL_USERNAME : default None
# MAIL_PASSWORD : default None
# MAIL_DEFAULT_SENDER : default None
# MAIL_MAX_EMAILS : default None
# MAIL_SUPPRESS_SEND : default app.testing
# MAIL_ASCII_ATTACHMENTS : default False
