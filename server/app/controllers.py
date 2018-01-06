from flask import Flask, jsonify, request, Response, send_from_directory
from flask_restful import Resource, Api, reqparse, url_for
from datetime import datetime, timedelta
import time
from utils import to_dict, before_write
from werkzeug import secure_filename
from os import path, makedirs
import models
from store import app
import hashlib
import random

# for get ,save and delete data
class ResourceController(Resource):
    # get data
    def get(self,model_name, id=None):
        # model class
        model = models.__dict__[model_name]
        if id:
            # return one row
            return {'data': to_dict(model.objects.filter(id=id).first())}
        else:
            # return resources list
            # default page: 1, per_page: 20
            page = int(request.args.get('page') or 1)
            per_page = int(request.args.get('per_page') or 20)
            start = (page - 1) * per_page
            end = page * per_page
            return {'data': to_dict(model.objects.all()[start:end])}
    # create a row; will check row if exist by id
    def post(self, model_name, id=None):
        model = models.__dict__[model_name]
        # make data
        data = {}
        for key in request.form:
            data[key] = request.form[key]
        before_write(data, model)
        data['created_at'] = data['updated_at'] = datetime.now()
        data['id'] = id or request.form['id']
        # check exits
        errorMsg = None
        item = model.objects(id = data['id']).first()
        if item:
            errorMsg = 'Item already exists'
        else:
            # write
            try:
                model.create(**data)
            except Exception as e:
                errorMsg = e.message
        return {'result': 'failed' if errorMsg else 'success', 'message': errorMsg}
    # update a row
    def put(self, model_name, id=None):
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
            errorMsg = e.message
        return {'result': 'failed' if errorMsg else 'success', 'message': errorMsg}
    # delete a row or many rows
    def delete(self, model_name, id=None):
        model = models.__dict__[model_name]
        ids = [id] if ',' not in id else id.split(',')
        try:
            model.objects.filter(id__in=ids).if_exists().delete()
        except Exception as e:
            errorMsg = e.message
        return {'result': 'failed' if errorMsg else 'success', 'message': errorMsg}
    # for cros non-get requests
    def options(self, model_name, id=None):
        return ''

# todo: get data with conditions
class QueryController(Resource):
    pass

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['file_allowedExtensions']
class FileController(Resource):
    def get(self, filename):
        return send_from_directory(app.config['file_uploadDir'], filename = filename)
    # upload file or files
    def post(self):
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            t, extension = path.splitext(filename)
            filename = datetime.now().strftime('/%Y/%m/%d/') + hashlib.md5((str(time.time()) + '_' + str(random.random()) + '_' + filename).encode('utf8')).hexdigest() + extension
            fullPath = path.join(app.config['file_uploadDir'], filename)
            makedirs(path.dirname(fullPath))
            file.save(fullPath)
            return {'result': 'success', 'data': filename}
        return {'result': 'failed', 'message': 'Disallowed file type' if file else 'No file'}, 400
