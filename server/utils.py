
def to_dict(arg):
    r = None
    if type(arg) == list:
        r = [dict(i) for i in arg]
    else:
        r = dict(arg)
    return r
def camel_case(st):
    output = ''.join(x for x in st.title() if x.isalpha())
    return output[0].lower() + output[1:]
def studly_case(st):
    return st[0].upper() + st[1:]

def model_data_write_guard(data):
    keys = ['id', 'created_at', 'updated_at']
    for key in keys:
        if key in data:
            del data[key]
    return data
