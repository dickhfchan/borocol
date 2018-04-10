import datetime,time,decimal,uuid, os, json
import string
import random
from cerberus import Validator
import hashlib
import bcrypt
from flask import current_app as app, request, render_template
import http.client, urllib.request, urllib.parse, urllib.error
import models
from flask_login import current_user
from plugins.middlewareHelper import stop
from urllib.parse import urlparse

def dict_pluck(data, keys):
    newDict = {}
    for key in keys:
        newDict[key] = data.get(key)
    return newDict

# quick read, write file
def file_get_contents(filename):
    with open(filename) as f:
        return f.read()
def file_put_contents(filename, content):
    with open(filename, 'w') as f:
        return f.write(content)

# get datetime columns from model class
# data: dict    model: class
def get_datetime_columns_from_model(model):
    # get model columns definition
    columns = model._defined_columns
    # find datetime columns; the db_type of datetime column is timestamp
    dt_columns = [colName for colName in columns if columns[colName].db_type == 'timestamp']
    return dt_columns

# get decimal columns from model class
# data: dict    model: class
def get_decimal_columns_from_model(model):
    # get model columns definition
    columns = model._defined_columns
    # find decimal columns
    dc_columns = [colName for colName in columns if columns[colName].db_type == 'decimal']
    return dc_columns

# convert str to camel case; eg: hello_world => helloWorld
def camel_case(st):
    output = ''.join(x for x in st.title() if x.isalpha())
    return output[0].lower() + output[1:]
# upper case first char of str
def studly_case(st):
    return st[0].upper() + st[1:]

# convert to dict; datetime to int, id to str, format decimal
def to_dict(item):
    from plugins.fileHelper import make_file_url
    columns = item._defined_columns
    r = {}
    for colName in columns:
        if hasattr(item, 'hidden') and colName in item.hidden:
            continue
        val = getattr(item, colName)
        if hasattr(item, 'file_fields') and colName in item.file_fields:
            val = make_file_url(val)
            r[colName] = val
        elif hasattr(item, 'json_fields') and colName in item.json_fields:
            val = json.loads(val) if val else None
            r[colName] = val
        elif isinstance(val, datetime.datetime):
            r[colName] = int(time.mktime(val.timetuple()))
        elif isinstance(val, decimal.Decimal):
            r[colName] = float((val or decimal.Decimal('0.00')).quantize(decimal.Decimal('0.00')))
        elif isinstance(val, uuid.UUID):
            r[colName] = str(val)
        else:
            r[colName] = val
    return r
def sort_models(models):
    models.sort(key=lambda item: item.created_at, reverse=True)
    return models

# before assign data to a model; remove keys maintenanced by backend; convert timestamp to datetime
# data0: dict    model: class
def before_write(model, data0):
    data = {}
    # pick fields in model
    columns = model._defined_columns
    for colName in columns:
        if colName in data0:
            data[colName] = data0[colName]
    # remove protected fields
    keys = ['created_at', 'updated_at']
    for key in keys:
        if key in data:
            del data[key]
    # convert timestamp to datetime beofore save
    dt_columns = get_datetime_columns_from_model(model)
    for col in dt_columns:
        if data.get(col):
            data[col] = datetime.datetime.fromtimestamp(data[col])
    # json fields to str
    if hasattr(model, 'json_fields'):
        for fld in model.json_fields:
            data[fld] = json.dumps(data[fld]) if data.get(fld) else None
    return data

# after row saved
def saved(item):
    if hasattr(item, 'file_fields'):
        files = [] # not empty
        for fld in item.file_fields:
            if isinstance(item[fld], (list, tuple)):
                files = files + item[fld]
            else:
                files.append(item[fld])
        for fp in files:
            item = models.file.objects.filter(path=fp).first()
            if item:
                item.tmp = False
                item.save()

# random string, from https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
def str_rand(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def md5(str0):
    return hashlib.md5(str0.encode('utf-8')).hexdigest()

# Validator
def make_validator(schema, allow_unknown = True):
    v = Validator(schema)
    v.allow_unknown = allow_unknown
    return v
emailSchema = {'required': True, 'type': 'string', 'regex': r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', 'maxlength': 255}
def keys_match(dc, keys):
    keys = keys[:]
    for k, v in dc.items():
        if k not in keys:
            return False
        else:
            keys.remove(k)
    return len(keys) == 0
def some(immutableVal, fun):
    for val in immutableVal:
        if fun(val):
            return val
    return False
# hash password
# return bytes
def hash_pwd(pwd):
    pwd = pwd.encode('utf-8')
    return bcrypt.hashpw(pwd, bcrypt.gensalt())
# pwd: str, hashed: bytes
def pwd_hashed_compare(pwd, hashed):
    pwd = pwd.encode('utf-8')
    return hashed == bcrypt.hashpw(pwd, hashed)

#
def success(message = '', data = None, code = 200):
    data2 = {'result': 'success', 'message': message}
    if data:
        data2 = dict(data2, **data)
    return data2, code
def failed(message = 'Failed', data = None, code = 400):
    data2 = {'result': 'failed', 'message': message}
    if data:
        data2 = dict(data2, **data)
    return data2, code
def trim_dict(dc):
    for k,v in dc.items():
        if isinstance(v, str):
            dc[k] = v.strip()

def request_json():
    data = request.get_json()
    if not data:
        return None
    for key in list(data.keys()):
        if isinstance(data[key], str):
            data[key] = data[key].strip()
    return data

def get_https_conn(domain):
    # use proxy
    if app.config['server_side_request_proxy']:
        conn = http.client.HTTPSConnection('localhost', '8118')
        conn.set_tunnel(domain)
    else:
        conn = http.client.HTTPSConnection(domain)
    return conn

def request_bytes(url, method = 'GET', *args):
    t = urlparse(url)
    if t.scheme != 'https':
        raise Exception('Only https supported')
    pathAndQuery = t.path
    if t.query:
        pathAndQuery += '?' + t.query
    try:
        conn = get_https_conn(t.netloc)
        conn.request(method, pathAndQuery, *args)
        bytesData = conn.getresponse().read()
    except Exception as e:
        raise e
    finally:
        conn.close()
    return bytesData

def fname(arg):
    pass

def validate_recaptcha(token):
    conn = None
    data = None
    errorMsg = None
    try:
        params = urllib.parse.urlencode({'secret': app.config['recaptcha_secretkey'], 'response': token})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = get_https_conn('www.google.com')
        conn.request('POST', '/recaptcha/api/siteverify', params, headers)
        data = conn.getresponse().read().decode('utf8')
    except Exception as e:
        print(e)
        errorMsg = str(e)
    finally:
        conn.close()
    if errorMsg:
        return errorMsg
    data = json.loads(data)
    if not data['success']:
        return data['error-codes']

def get_user_profile(user):
    model = models.student_profile if user.user_type == 'student' else models.school_profile
    return model.objects.filter(user_id=user.id).first()

def user_to_dict(user):
    item = to_dict(user)
    item['is_authenticated'] = user.is_authenticated
    item['is_anonymous'] = user.is_anonymous
    profile = to_dict(get_user_profile(user))
    item['avatar'] = profile['avatar']
    item['name'] = '%s %s %s'%(profile['first_name'], profile['middle_name'] or '', profile['last_name'])
    item['name'] = item['name'].replace('  ', ' ')
    return item

def bubble_sort(list0, func):
    # 冒泡排序
    list1 = list0[:]
    count = len(list1)
    for i in range(0, count):
        for j in range(i + 1, count):
            if func(list1[i], list1[j]) > 0:
                list1[i], list1[j] = list1[j], list1[i]
    return list1
