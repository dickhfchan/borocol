from os import path
from plugins.env import env
# db
db_keyspace = "borocol"
db_host = '127.0.0.1'
# app
app_debug = env('app_debug', False)
app_host = '127.0.0.1' # dev
app_port = 8081 # dev
app_name = 'Borocol'
app_path = path.dirname(__file__)
app_key = '\xfe\xfc\x8a\xebq>\xd4\x88\xa6\xccvkN,\xb89\xa9\xd97\xba\xb3R\x08\x1d'
# site
site_name = app_name
site_home_title = site_name
# api
api_prefix = '/api/v1'
# request
request_maxContentLength = 16 * 1024 * 1024 # 16m MAX_CONTENT_LENGTH
# file
file_uploadDir = path.join(app_path, 'uploads')
file_allowedExtensions = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'webp'])
# google recaptcha
recaptcha_proxy = env('recaptcha_proxy', False)
recaptcha_sitekey = '6LdizkgUAAAAANJGphKgKtGcERgbagwAAL91kti4'
recaptcha_secretkey = '6LdizkgUAAAAAB_bXXnjnjWomYSTy4GxVn7umQnf'
# mail
MAIL_SERVER = env('MAIL_SERVER', 'smtp.mailtrap.io')
MAIL_PORT = env('MAIL_PORT', '2525')
MAIL_USERNAME = env('MAIL_USERNAME', '0ae55e5821a6db')
MAIL_PASSWORD = env('MAIL_PASSWORD', '51593ff1131ed6')
MAIL_DEFAULT_SENDER_NAME = env('MAIL_DEFAULT_SENDER_NAME', site_name)
MAIL_DEFAULT_SENDER_ADDRESS = env('MAIL_DEFAULT_SENDER_ADDRESS', '')
MAIL_DEFAULT_SENDER = MAIL_DEFAULT_SENDER_NAME, MAIL_DEFAULT_SENDER_ADDRESS
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
