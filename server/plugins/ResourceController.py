from flask import request
from datetime import datetime
import time
from utils import to_dict, sort_models, before_write, saved, request_json
import utils as ut
import cassandra

def store(model, data):
    # make data
    data = before_write(model, data)
    data['created_at'] = data['updated_at'] = datetime.now()
    data['id'] = cassandra.util.uuid_from_time(time.time())
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
    def beforeUpdate(self, item):
        return True
    def beforeDestroy(self, items):
        return True
    # get data
    def select(self, id=None, *args, **kwargs):
        model = self.model
        data = request_json()
        if not id:
            id = data.get('id')
        if id:
            # return one row
            item = model.objects.filter(id=id).first()
            return ut.success(data=to_dict(item)) if item else ut.failed('Not found', code=404)
        else:
            # return resources list
            # default page: 1, per_page: 20
            page = int(request.args.get('page') or 1)
            per_page = int(request.args.get('per_page') or 20)
            start = (page - 1) * per_page
            end = page * per_page
            models = model.objects.all()[start:end]
            modelsDict = [to_dict(item) for item in models]
            return ut.success(modelsDict)
    # create a row; will check row if exist by id
    def store(self, *args, **kwargs):
        errorMsg = None
        item = None
        try:
            item = store(self.model, request_json())
        except Exception as e:
            print(e)
            errorMsg = str(e)
        return ut.failed(errorMsg) if errorMsg else ut.success(append={'id': str(item.id)})
    # update a row
    def update(self, *args, **kwargs):
        errorMsg = None
        data = request_json()
        id = data.get('id')
        item = self.model.objects(id=id).first()
        if not item:
            return ut.failed('Not found', code=404)
        if not self.beforeUpdate(item):
            return ut.failed()
        try:
            item = update(self.model, data, id)
        except Exception as e:
            errorMsg = str(e)
        return ut.failed(errorMsg) if errorMsg else ut.success()
    # delete a row or many rows
    def destroy(self, *args, **kwargs):
        model = self.model
        data = request_json()
        id = data.get('id')
        ids = [id] if ',' not in id else id.split(',')
        errorMsg = None
        try:
            items = model.objects.filter(id__in=ids)[:]
            if not self.beforeDestroy(items):
                return ut.failed()
            model.objects.filter(id__in=ids).delete()
        except Exception as e:
            errorMsg = str(e)
        return ut.failed(errorMsg) if errorMsg else ut.success()
