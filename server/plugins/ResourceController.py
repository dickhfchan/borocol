from flask import request
from datetime import datetime
import time
from utils import to_dict, sort_models, before_write, saved, request_json
import cassandra

def store(model, data):
    # make data
    data = before_write(model, data)
    data['created_at'] = data['updated_at'] = datetime.now()
    data['id'] = cassandra.util.uuid_from_time(time.time())
    errorMsg = None
    item = None
    # save
    item = model.create(**data)
    saved(item)
    return item

def update(model, data, id):
    # make data
    data = before_write(model, data)
    data['updated_at'] = datetime.now()
    # prevent change id
    if 'id' in data:
        del data['id']
    # write
    model.objects(id=id).update(**data)
    item = model.objects(id=id).first()
    saved(item)
    return item

# for get ,save and delete data
class ResourceController(object):
    model = None
    # get data
    def select(self, id=None, *args, **kwargs):
        model = self.model
        data = request_json()
        if not id:
            id = data.get('id')
        if id:
            # return one row
            item = model.objects.filter(id=id).first()
            return {'result': 'success', 'data': to_dict(item)} if item else ({'result': 'failed', 'message': 'Not found'}, 400)
        else:
            # return resources list
            # default page: 1, per_page: 20
            page = int(request.args.get('page') or 1)
            per_page = int(request.args.get('per_page') or 20)
            start = (page - 1) * per_page
            end = page * per_page
            models = model.objects.all()[start:end]
            modelsDict = [to_dict(item) for item in models]
            return {'result': 'success', 'data': modelsDict}
    # create a row; will check row if exist by id
    def store(self, *args, **kwargs):
        errorMsg = None
        item = None
        try:
            item = store(self.model, request_json())
        except Exception as e:
            print(e)
            errorMsg = str(e)
        return ({'result': 'failed', 'message': errorMsg}, 400) if errorMsg else {'result': 'success', 'id': str(item.id)}
    # update a row
    def update(self, id, *args, **kwargs):
        errorMsg = None
        item = None
        try:
            item = update(self.model, request_json(), id)
        except Exception as e:
            errorMsg = str(e)
        return ({'result': 'failed', 'message': errorMsg}, 400) if errorMsg else {'result': 'success'}
    # delete a row or many rows
    def destroy(self, id, *args, **kwargs):
        model = self.model
        ids = [id] if ',' not in id else id.split(',')
        errorMsg = None
        try:
            model.objects.filter(id__in=ids).delete()
        except Exception as e:
            errorMsg = str(e)
        return ({'result': 'failed', 'message': errorMsg}, 400) if errorMsg else {'result': 'success'}
