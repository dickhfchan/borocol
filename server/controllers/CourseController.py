from flask import current_app as app, request
import models
from plugins.ResourceController import ResourceController, store
import cassandra
from utils import request_json
import utils as ut
from flask_login import current_user

class CourseController(ResourceController):
    model = models.course
    def beforeWrite(self, data, type):
        self.data = data
        # 
        if current_user.user_type != 'school':
            return ut.failed('Only schools can create courses')
        # 
        data['school_id'] = current_user.id
        # validate
        schema = {
            #
            'with_accom': {'required': True, 'type': 'boolean'},
            #
            'start_date': {'required': True, 'type': 'number'},
            'end_date': {'required': True, 'type': 'number'},
            'category_id': {'required': True, 'type': 'string', 'maxlength': 255},
            'level': {'required': True, 'type': 'string', 'maxlength': 255},
            'title': {'required': True, 'type': 'string', 'maxlength': 255},
            #
            'gender': {'required': True, 'type': 'string', 'maxlength': 255},
            'age_range': {'required': True, 'type': 'list'},
            'hours': {'required': True, 'type': 'list'},
            'description': {'required': True, 'type': 'string', 'maxlength': 10000},
            #
            'language': {'required': True, 'type': 'string', 'maxlength': 255},
            #
            'street': {'required': True, 'type': 'string', 'maxlength': 255},
            'city': {'required': True, 'type': 'string', 'maxlength': 255},
            'province': {'required': True, 'type': 'string', 'maxlength': 255},
            'zip_code': {'required': True, 'type': 'string', 'maxlength': 255},
            'country': {'required': True, 'type': 'string', 'maxlength': 255},
            'api_key': {'required': True, 'type': 'string', 'maxlength': 255},
            'location_description': {'required': True, 'type': 'string', 'maxlength': 10000},
            'how_to_get_there': {'required': True, 'type': 'string', 'maxlength': 10000},
            'where_to_meet': {'required': True, 'type': 'string', 'maxlength': 10000},
            #
            'schedule': {'required': True, 'type': 'string', 'maxlength': 10000},
            'meals_included': {'required': True, 'type': 'boolean'},
            'meals': {'required': True, 'type': 'list'},
            #
            'issue_certificate': {'required': True, 'type': 'boolean'},
            #
            'request_form_enabled': {'required': True, 'type': 'boolean'},
            #
            #
            'group_size': {'required': True, 'type': 'number'},
            'seat_quota': {'required': True, 'type': 'number'},
            'price': {'required': True, 'type': 'number'},
            #
            #
            'cover': {'required': True, 'type': 'string', 'maxlength': 255},
            'photos': {'required': True, 'type': 'list', 'minlength': 2},
        }
        v = ut.make_validator(schema)
        if not v.validate(data):
            return ut.failed('Invalid input', {'error': v.errors})
        # validate instructors meals certificate request_form price early_bird down_payment
        t = data['instructors']
        if not ut.keys_match(t, ["name","phone","description","photo"]):
            return ut.failed('Invalid input')
        k = ut.dict_any_key_none(t[0])
        if k:
            return ut.failed('The %s of main instructor is required.'%(k.replace('_', ' ')))
        if data['meals_included']:
            if len(data['meals']) == 0:
                return ut.failed('The meals is required.')
        if data['issue_certificate']:
            if not data['certificate']:
                return ut.failed('The certificate is required.')
        if data['request_form_enabled']:
            if data['request_form'][0]['enabled'] and not data['request_form'][0]['value']:
                return ut.failed('Request form 1 is required.')
            if data['request_form'][1]['enabled'] and not data['request_form'][1]['value']:
                return ut.failed('Request form 2 is required.')
        if not data['with_accom']:
            if data['price'] == None:
                return ut.failed('The price is required.')
        if data['early_bird']['enabled']:
            k = ut.dict_any_key_none(data['early_bird'])
            if k:
                return ut.failed('The %s of early bird is required.'%(k.replace('_', ' ')))
        if data['down_payment']['enabled']:
            k = ut.dict_any_key_none(data['down_payment'])
            if k:
                return ut.failed('The %s of down payment is required.'%(k.replace('_', ' ')))
        # accomodation
        if data['with_accom']:
            schema = {
                'type': {'required': True, 'type': 'string'},
                'name': {'required': True, 'type': 'string'},
                'phone': {'required': True, 'type': 'string'},
                'address': {'required': True, 'type': 'string'},
                'facilities': {'required': True, 'type': 'list'},
                'description': {'required': True, 'type': 'string', 'maxlength': 10000},
                'photos': {'required': True, 'type': 'list'},
            }
            v = ut.make_validator(schema)
            if not v.validate(data['accomodation']):
                return ut.failed('Invalid input for accomodation', {'error': v.errors})
            roomCount = 0
            for i, v in enumerate(data['accomodation']['rooms']):
                if v['enabled']:
                    roomCount += 1
                    k = ut.dict_any_key_none(v)
                    if k:
                        return ut.failed('The %s of room %s is required.'%(k.replace('_', ' '), i + 1))
            if roomCount == 0:
                return ut.failed('At least one enabled room is needed')
    def store(self):
        r = super().store()[0]
        # may failed
        if r['result'] == 'success':
            data = self.data['accomodation']
            data['course_id'] = r['id']
            item = None
            # save
            try:
                item = store(models.accomodation, data)
                r['accomodation_id'] = str(item.id)
                return ut.success(append=r)
            except Exception as e:
                print(666)
                app.logger.debug(e)
                print(e)
                return ut.failed(str(e))
        else:
            return ut.failed(append=r)
