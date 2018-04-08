from flask import current_app as app, request, send_from_directory
from plugins.fileHelper import make_filename, make_fullpath, make_dir_by_path
from plugins.ResourceController import store, update
import models

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['file_allowedExtensions']

class FileController():
    def get_file(self, year, month, date, filename):
        return send_from_directory('%s/%s/%s/%s'%(app.config['file_uploadDir'], year, month, date), filename = filename)
    # upload file
    def store(self):
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = make_filename(file.filename)
            fullPath = make_fullpath(filename)
            make_dir_by_path(fullPath)
            # save
            file.save(fullPath)
            # mark temperature
            # todo not deleteTmpFiles
            if not models.file.objects.filter(path=filename).first():
                store(models.file, {'path': filename, 'tmp': True})
            return {'result': 'success', 'data': filename}
        return {'result': 'failed', 'message': 'Disallowed file type' if file else 'No file'}, 400
