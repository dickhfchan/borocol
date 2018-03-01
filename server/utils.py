import datetime,time,decimal,uuid, os, json
import string
import random
from cerberus import Validator
import bcrypt
from flask import current_app as app, request, render_template
import http.client, urllib.request, urllib.parse, urllib.error
import models
from flask_login import current_user

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
    columns = item._defined_columns
    r = {}
    for colName in columns:
        if hasattr(item, 'hidden') and colName in item.hidden:
            continue
        val = getattr(item, colName)
        if isinstance(val, datetime.datetime):
            r[colName] = int(time.mktime(val.timetuple()))
        elif isinstance(val, decimal.Decimal):
            r[colName] = float((val or decimal.Decimal('0.00')).quantize(decimal.Decimal('0.00')))
        elif isinstance(val, uuid.UUID):
            r[colName] = str(val)
        else:
            r[colName] = val
    return r

# tmp files
def add_tmp_files(files):
    from flask import current_app as app
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
    from flask import current_app as app
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
    return data

# after row saved
def saved(item):
    if hasattr(item, 'fileFields'):
        files = [] # not empty
        for fld in item.fileFields:
            if isinstance(item[fld], (list, tuple)):
                files = files + item[fld]
            else:
                files.append(item[fld])
        deleteTmpFiles(files)

# random string, from https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python
def str_rand(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Validator
def make_validator(schema, allow_unknown = True):
    v = Validator(schema)
    v.allow_unknown = allow_unknown
    return v

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
def failed(message = '', data = None, code = 400):
    data2 = {'result': 'failed', 'message': message}
    if data:
        data2 = dict(data2, **data)
    return data2, code

def request_json():
    data = request.get_json()
    for key in list(data.keys()):
        if isinstance(data[key], str):
            data[key] = data[key].strip()
            if data[key] == '':
                data[key] = None
    return data

def validate_recaptcha(token):
    conn = None
    data = None
    try:
        params = urllib.parse.urlencode({'secret': app.config['recaptcha_secretkey'], 'response': token})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        # use proxy
        # conn = http.client.HTTPSConnection('localhost', '8118')
        # conn.set_tunnel("www.google.com")
        conn = http.client.HTTPSConnection('www.google.com')
        conn.request('POST', '/recaptcha/api/siteverify', params, headers)
        data = conn.getresponse().read()
    except Exception as e:
        raise e
    finally:
        if conn:
            conn.close()
    return json.loads(data)

def get_user_profile(user):
    model = models.student_profile if user.user_type == 'student' else models.school_profile
    return model.objects.filter(user_id=user.id).first()

def user_to_dict(user):
    item = to_dict(user)
    item['is_authenticated'] = user.is_authenticated
    item['is_anonymous'] = user.is_anonymous
    profile = get_user_profile(user)
    item['avatar'] = profile.avatar
    item['name'] = '%s %s %s'%(profile.first_name, profile.middle_name or '', profile.last_name)
    item['name'] = item['name'].replace('  ', ' ')
    return item

def render_spa(fp, initialDataAppend = None):
    html = render_template(fp)
    initialData = {'serverRoot': '', 'clientBase': '/'} # serverRoot cant end with /
    initialData['recaptcha'] = {'sitekey': app.config['recaptcha_sitekey']}
    # inject user info
    if current_user.is_authenticated:
        initialData['authenticated'] = True
        initialData['user'] = user_to_dict(current_user)
    #
    if initialDataAppend:
        initialData.update(initialDataAppend)
    #
    html = html.replace('<head>', '<head><script>var initialData = %s;</script>'%(json.dumps(initialData)))
    return html
