from flask import Flask, jsonify, request, Response, send_from_directory, current_app as app
from flask_restful import Resource, Api, reqparse, url_for
from datetime import datetime, timedelta
import time
from utils import to_dict, before_write, addTmpFiles, deleteTmpFiles
from werkzeug import secure_filename
from os import path, makedirs
import models
import hashlib
import random
import json
import cassandra

# for get ,save and delete data
class ResourceController(Resource):
    model_name = None
    # get data
    def get(self,model_name = None, id=None):
        if self.model_name:
            model_name = self.model_name
        # model class
        model = models.__dict__[model_name]
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
            return {'result': 'success', 'data': to_dict(model.objects.all()[start:end])}
    # create a row; will check row if exist by id
    def post(self, model_name = None, id=None):
        if self.model_name:
            model_name = self.model_name
        model = models.__dict__[model_name]
        # make data
        data = before_write(request.get_json(), model)
        data['created_at'] = data['updated_at'] = datetime.now()
        data['id'] = cassandra.util.uuid_from_time(time.time())
        errorMsg = None
        item = None
        # save
        try:
            item = model.create(**data)
        except Exception as e:
            print(e)
            errorMsg = str(e)
        return ({'result': 'failed', 'message': errorMsg}, 400) if errorMsg else {'result': 'success', 'id': str(item.id)}
    # update a row
    def put(self, model_name = None, id=None):
        if self.model_name:
            model_name = self.model_name
        model = models.__dict__[model_name]
        # make data
        data = {}
        for key in request.form:
            data[key] = request.form[key]
        before_write(data, model)
        data['updated_at'] = datetime.now()
        del data['id'] # prevent change id
        # write
        errorMsg = None
        try:
            model.objects(id=id).if_exists().update(**data)
        except Exception as e:
            errorMsg = str(e)
        return ({'result': 'failed', 'message': errorMsg}, 400) if errorMsg else {'result': 'success'}
    # delete a row or many rows
    def delete(self, model_name = None, id=None):
        if self.model_name:
            model_name = self.model_name
        model = models.__dict__[model_name]
        ids = [id] if ',' not in id else id.split(',')
        errorMsg = None
        try:
            model.objects.filter(id__in=ids).delete()
        except Exception as e:
            errorMsg = str(e)
        return ({'result': 'failed', 'message': errorMsg}, 400) if errorMsg else {'result': 'success'}
    # for cros non-get requests
    def options(self, model_name, id=None):
        return ''

# todo: get data with conditions
class QueryController(Resource):
    pass

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['file_allowedExtensions']
class FileController(Resource):
    def get(self, year, month, date, filename):
        return send_from_directory('%s/%s/%s/%s'%(app.config['file_uploadDir'], year, month, date), filename = filename)
    # upload file
    def post(self):
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            t, extension = path.splitext(filename)
            filename = datetime.now().strftime('~/%Y/%m/%d/') + hashlib.md5((str(time.time()) + '_' + str(random.random()) + '_' + filename).encode('utf8')).hexdigest() + extension
            fullPath = filename.replace('~', app.config['file_uploadDir'])
            # make dirname if not exists
            dirname = path.dirname(fullPath)
            if not path.exists(dirname):
                makedirs(dirname)
            # save
            file.save(fullPath)
            # mark temperature
            addTmpFiles([filename])
            return {'result': 'success', 'data': filename}
        return {'result': 'failed', 'message': 'Disallowed file type' if file else 'No file'}, 400

class CourseDetailController(ResourceController):
    """docstring for CourseDetailController."""
    model_name = 'course_detail'
    def __init__(self):
        super(CourseDetailController, self).__init__()
    def post(self):
        r = super().post()
        if isinstance(r, (tuple, list)):
            r = r[0]
        if r['result'] == 'success':
            cd = models.course_detail.objects.filter(id=r['id']).first()
            model = models.accomodation_detail
            data = before_write(request.get_json()['accomodation_detail'], model)
            data['created_at'] = data['updated_at'] = datetime.now()
            data['id'] = cassandra.util.uuid_from_time(time.time())
            data['course_id'] = r['id']
            item = None
            # save
            try:
                item = model.create(**data)
                r['accomodation_detail_id'] = str(item.id)
                # move files out of tmp
                files = [cd.instructor_photo, cd.cover] + cd.photos + item.photos
                deleteTmpFiles(files)
            except Exception as e:
                print(e)
                r['message'] = str(e)
                r['result'] = 'failed'
        return (r, 400) if r['result'] == 'failed' else r
