import datetime,time,decimal,uuid, os, json

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

# row is a model
# convert row to dict; then convert datetime column to int
def row2dict(row):
    r = dict(row)
    for k in r:
        t = type(r[k])
        if t == datetime.datetime:
            r[k] = int(time.mktime(r[k].timetuple()))
        elif t == decimal.Decimal:
            r[k] = float((r[k] or decimal.Decimal('0.00')).quantize(decimal.Decimal('0.00')))
        elif t == uuid.UUID:
            r[k] = str(r[k])
    return r

# convert a model or models list to dict or dict list
def to_dict(arg):
    r = None
    if type(arg) == list:
        r = [row2dict(i) for i in arg]
    else:
        r = row2dict(arg)
    return r
# convert str to camel case; eg: hello_world => helloWorld
def camel_case(st):
    output = ''.join(x for x in st.title() if x.isalpha())
    return output[0].lower() + output[1:]
# upper case first char of str
def studly_case(st):
    return st[0].upper() + st[1:]

# before assign data to a model; remove keys maintenanced by backend; convert timestamp to datetime
# data0: dict    model: class
def before_write(data0, model):
    data = {}
    # pick fields in model
    columns = model._defined_columns
    for colName in columns:
        data[colName] = data0.get(colName)
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

# tmp files
def addTmpFiles(files):
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
def deleteTmpFiles(files):
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
