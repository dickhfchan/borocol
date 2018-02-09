from flask import current_app as app, request
import models
from ResourceController import ResourceController, store
import cassandra

class CourseDetailController(ResourceController):
    model = models.course_detail
    def store(self):
        r = super().store()
        model = self.model
        # may failed
        if isinstance(r, (tuple, list)):
            r = r[0]
        if r['result'] == 'success':
            data = request.get_json()['accomodation_detail']
            data['course_id'] = r['id']
            item = None
            # save
            try:
                item = store(models.accomodation_detail, data)
                r['accomodation_detail_id'] = str(item.id)
            except Exception as e:
                print(e)
                r['message'] = str(e)
                r['result'] = 'failed'
        return (r, 400) if r['result'] == 'failed' else r
