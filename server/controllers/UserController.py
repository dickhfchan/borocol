from flask import current_app as app, request
import models
from ResourceController import ResourceController, store
from utils import failed, success, make_validator, hash_pwd, hash_compare, dict_pluck, request_json

class UserController(ResourceController):
    model = models.user
    def register(self):
        schema = {
            'email': {'required': True, 'type': 'string', 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', 'maxlength': 255},
            'first_name': {'required': True, 'type': 'string', 'maxlength': 255},
            'last_name': {'required': True, 'type': 'string', 'maxlength': 255},
            'password': {'required': True, 'type': 'string', 'maxlength': 255},
            # 'user_type': {'required': True, 'type': 'string', 'allowed': ['school', 'student']},
        }
        v = make_validator(schema)
        data = request_json()
        if not v.validate(data):
            return failed('Invalid input', {'error': v.errors})
        if data.get('user_type') != 'student':
            return failed('Invalid user_type')
        if self.model.objects.filter(email=data['email']).first():
            return failed('Email already exists')
        data['password'] = hash_pwd(data['password'])
        try:
            user = store(self.model, data)
            profileData = dict_pluck(data, ['first_name', 'last_name'])
            profile = store(models.student_profile, profileData)
        except Exception as e:
            print(e)
            errorMsg = str(e)
        if 'errorMsg' in locals():
            return failed(errorMsg)
        return success('', {'id': str(user.id)})
