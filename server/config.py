from os import path

debug = True
# db
db_keyspace = "borocol"
db_host = '127.0.0.1'
# app
app_host = '0.0.0.0'
app_port = 8081
app_name = 'Borocol'
app_path = path.dirname(__file__)
# request
request_maxContentLength = 16 * 1024 * 1024 # 16m MAX_CONTENT_LENGTH
# file
file_uploadDir = path.join(app_path, 'uploads')
file_allowedExtensions = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'webp'])
