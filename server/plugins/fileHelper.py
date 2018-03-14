from flask import current_app as app
from datetime import datetime, timedelta
import time
import hashlib
import random
from os import path, makedirs
import json

def make_filename(filename):
    t, extension = path.splitext(filename)
    filename = datetime.now().strftime('~/%Y/%m/%d/') + hashlib.md5((str(time.time()) + '_' + str(random.random()) + '_' + filename).encode('utf8')).hexdigest() + extension
    return filename

def make_fullpath(fullPath):
    if fullPath[0] == '~':
        fullPath = app.config['file_uploadDir'] + fullPath[1:]
    return fullPath

def make_dir_by_path(fullPath):
    dirname = path.dirname(fullPath)
    if not path.exists(dirname):
        makedirs(dirname)

# tmp files
def add_tmp_files(files):
    tmpPath = app.config['file_uploadDir'] + '/tmp.json'
    tmp = {}
    if os.path.exists(tmpPath):
        f = open(tmpPath, 'r')
        tmp = json.load(f)
        f.close()
    f = open(tmpPath, 'w')
    for fn in files:
        tmp[fn] = int(time.time())
    json.dump(tmp,f)
    f.close()
def delete_tmp_files(files):
    tmpPath = app.config['file_uploadDir'] + '/tmp.json'
    tmp = {}
    if os.path.exists(tmpPath):
        f = open(tmpPath, 'r')
        tmp = json.load(f)
        f.close()
    f = open(tmpPath, 'w')
    for fn in files:
        if fn in tmp:
            del tmp[fn]
    json.dump(tmp,f)
    f.close()
