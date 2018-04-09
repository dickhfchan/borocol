from os import path
# lower case name first

# db
db_keyspace = "borocol"
db_host = '127.0.0.1'
# app
app_debug = False
app_host = '127.0.0.1' # dev
app_port = 8081 # dev
tornado_port = 8081 # prod
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
# for server to access google or other api
server_side_request_proxy = False
# mail
MAIL_SERVER = 'smtp.mailtrap.io'
MAIL_PORT = '2525'
MAIL_USERNAME = '0ae55e5821a6db'
MAIL_PASSWORD = '51593ff1131ed6'
MAIL_DEFAULT_SENDER_NAME = site_name
MAIL_DEFAULT_SENDER_ADDRESS = ''
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

# overwrite with env
from env import *
