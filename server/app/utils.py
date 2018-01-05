import time
import datetime

# get datetime columns from model class
# data: dict    model: class
def get_datetime_columns_from_model(model):
    # get model columns definition
    columns = model._defined_columns
    # find datetime columns; the db_type of datetime column is timestamp
    dt_columns = [colName for colName in columns if columns[colName].db_type == 'timestamp']
    return dt_columns

# row is a model
# convert row to dict; then convert datetime column to int
def row2dict(row):
    r = dict(row)
    dt_columns = get_datetime_columns_from_model(type(row))
    for col in dt_columns:
        r[col] = int(time.mktime(r[col].timetuple()))
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
# data: dict    model: class
def before_write(data, model):
    keys = ['created_at', 'updated_at']
    for key in keys:
        if key in data:
            del data[key]
    # convert timestamp to datetime beofore save
    dt_columns = get_datetime_columns_from_model(model)
    for col in dt_columns:
        if col in data:
            data[col] = datetime.datetime.fromtimestamp(data[col])
    return data
