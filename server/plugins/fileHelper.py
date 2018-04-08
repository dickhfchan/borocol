from flask import current_app as app, url_for
from datetime import datetime, timedelta
import time
import hashlib
import random
from os import path, makedirs
import json
from utils import request_bytes

def make_filename(filename):
    t, extension = path.splitext(filename)
    filename = datetime.now().strftime('~/%Y/%m/%d/') + hashlib.md5((str(time.time()) + '_' + str(random.random()) + '_' + filename).encode('utf8')).hexdigest() + extension
    return filename

def make_fullpath(fullPath):
    if fullPath[0] == '~':
        fullPath = app.config['file_uploadDir'] + fullPath[1:]
    return fullPath

def make_file_url(url):
    if url and url[0] == '~':
        y, m, d, fn = url[2:].split('/')
        url = url_for('getFile', year=y, month=m,date=d,filename=fn)
    return url

def make_dir_by_path(fullPath):
    dirname = path.dirname(fullPath)
    if not path.exists(dirname):
        makedirs(dirname)

def save_remote_pic(url):
    data = request_bytes(url)
    filename = make_filename(url)
    fullPath = make_fullpath(filename)
    make_dir_by_path(fullPath)
    with open(fullPath, "wb") as file:
        file.write(data)
    return filename
