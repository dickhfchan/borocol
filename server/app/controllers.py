from flask import Flask, jsonify, request, Response
from flask_restful import Resource, Api, reqparse
from datetime import datetime, timedelta
from utils import to_dict, before_write
import models

# for get ,save and delete data
class ResourceController(Resource):
    # get data
    def get(self,model_name, id=None):
        # model class
        model = models.__dict__[model_name]
        if id:
            # return one row
            return {'resource': to_dict(model.objects.filter(id=id).first())}, 200
        else:
            # return resources list
            # default page: 1, per_page: 20
            page = int(request.args.get('page') or 1)
            per_page = int(request.args.get('per_page') or 20)
            start = (page - 1) * per_page
            end = page * per_page
            return {'resources': to_dict(model.objects.all()[start:end])}, 200
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
        return {'result': 'failed' if errorMsg else 'success', 'message': errorMsg}, 200
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
        return {'result': 'failed' if errorMsg else 'success', 'message': errorMsg}, 200
    # delete a row or many rows
    def delete(self, model_name, id=None):
        model = models.__dict__[model_name]
        ids = [id] if ',' not in id else id.split(',')
        try:
            model.objects.filter(id__in=ids).if_exists().delete()
        except Exception as e:
            errorMsg = e.message
        return {'result': 'failed' if errorMsg else 'success', 'message': errorMsg}, 200
    # for cros non-get requests
    def options(self, model_name, id=None):
        return '', 200

# todo: get data with conditions
class QueryController(Resource):
    pass

class FileController(Resource):
    def get(self):
        return {'resources': '666'}, 200
    # upload file or files
    def post(self):
        print(request.files['a'])
        # file = request.files['file']
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #     return redirect(url_for('uploaded_file',
        #                             filename=filename))
        # model = models.__dict__[model_name]
        # # make data
        # data = {}
        # for key in request.form:
        #     data[key] = request.form[key]
        # before_write(data, model)
        # data['created_at'] = data['updated_at'] = datetime.now()
        # data['id'] = id or request.form['id']
        # # check exits
        # errorMsg = None
        # item = model.objects(id = data['id']).first()
        # if item:
        #     errorMsg = 'Item already exists'
        # else:
        #     # write
        #     try:
        #         model.create(**data)
        #     except Exception as e:
        #         errorMsg = e.message
        # return {'result': 'failed' if errorMsg else 'success', 'message': errorMsg}, 200
    pass
