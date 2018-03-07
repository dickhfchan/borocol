from flask import current_app as app, request, send_from_directory
from plugins.ResourceController import ResourceController
from datetime import datetime, timedelta
import time
import hashlib
import random
from os import path, makedirs
from utils import add_tmp_files

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['file_allowedExtensions']
class FileController(ResourceController):
    def find(self, year, month, date, filename):
        return send_from_directory('%s/%s/%s/%s'%(app.config['file_uploadDir'], year, month, date), filename = filename)
    # upload file
    def store(self):
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = file.filename
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
            add_tmp_files([filename])
            return {'result': 'success', 'data': filename}
        return {'result': 'failed', 'message': 'Disallowed file type' if file else 'No file'}, 400
