from os import path

debug = path.exists('./.dev')
# db
db_keyspace = "borocol"
db_host = '127.0.0.1'
# app
app_host = '0.0.0.0' # dev
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
