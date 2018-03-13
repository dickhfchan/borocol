from flask import current_app as app, request
import models
from plugins.ResourceController import ResourceController, store
import cassandra
from utils import request_json

class CourseController(ResourceController):
    model = models.course
    def store(self):
        r = super().store()
        model = self.model
        # may failed
        if isinstance(r, (tuple, list)):
            r = r[0]
        if r['result'] == 'success':
            data = request_json()['accomodation']
            data['course_id'] = r['id']
            item = None
            # save
            try:
                item = store(models.accomodation, data)
                r['accomodation_id'] = str(item.id)
            except Exception as e:
                print(e)
                r['message'] = str(e)
                r['result'] = 'failed'
        return (r, 400) if r['result'] == 'failed' else r
