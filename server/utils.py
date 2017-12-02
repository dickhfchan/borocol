import time

def row2dict(row):
    r = dict(row)
    columns = type(row)._defined_columns
    # datetime db_type is timestamp
    dt_columns = [colName for colName in columns if columns[colName].db_type == 'timestamp']
    for col in dt_columns:
        r[col] = int(time.mktime(r[col].timetuple()))
    return r

def to_dict(arg):
    r = None
    if type(arg) == list:
        r = [row2dict(i) for i in arg]
    else:
        r = row2dict(arg)
    return r

def camel_case(st):
    output = ''.join(x for x in st.title() if x.isalpha())
    return output[0].lower() + output[1:]
def studly_case(st):
    return st[0].upper() + st[1:]

def before_write(data, model):
    keys = ['id', 'created_at', 'updated_at']
    for key in keys:
        if key in data:
            del data[key]
    # todo convert timestamp to datetime beofore save
    print 'todo convert timestamp to datetime beofore save'
    return data
