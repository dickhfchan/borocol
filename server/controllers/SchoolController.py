from flask import current_app as app, request, render_template, url_for, redirect
import models
from plugins.ResourceController import ResourceController, store, update
from utils import failed, success, make_validator, hash_pwd, pwd_hashed_compare
from utils import dict_pluck, request_json, to_dict, sort_models, validate_recaptcha
from utils import str_rand, user_to_dict, md5, get_user_profile, rules, keys_match, some
from flask_login import login_user, logout_user, current_user
from plugins.mail import mail
from flask_mail import Message
from datetime import datetime
import json

# this file has 2 controllers AuthController, UserController

class SchoolController(ResourceController):
    model = models.user
    def register(self):
        data = request_json()
        # recaptcha
        errorMsg = validate_recaptcha(data['recaptcha'])
        if errorMsg:
            return failed(errorMsg)
        #
        schema = {
            'name': {'required': True, 'type': 'string', 'maxlength': 255},
            'address': {'required': True, 'type': 'string', 'maxlength': 255},
            'city': {'required': True, 'type': 'string', 'maxlength': 255},
            'country': {'required': True, 'type': 'string', 'maxlength': 255},
            'email': rules['email'],
            'introduction': {'required': True, 'type': 'string', 'maxlength': 1000},
            'website': {'required': True, 'type': 'string', 'maxlength': 1000},
            'contact_persons': {'required': True, 'maxlength': 1000},
            'registration_document': {'required': True, 'maxlength': 1000},
        }
        v = make_validator(schema)
        if not v.validate(data):
            return failed('Invalid input', {'error': v.errors})
        try:
            t = data['contact_persons']
            keys = ['last_name', 'first_name', 'title', 'email', 'tel']
            if not keys_match(t[0], keys) or not keys_match(t[1], keys):
                return failed('Invalid input')
            for k, v in t[0].items():
                if not v:
                    return failed('The %s is required.'%(k.replace('_', ' ')))
        except Exception as e:
            app.logger.debug(e)
            return failed('Invalid input')
        #
        user = self.model.objects.filter(email=data['email']).first()
        if user:
            return failed('An account with this email already exists')
        userData = {
            'email': data['email'],
            'password': hash_pwd(str_rand(16)),
            'user_type': 'school',
        }
        try:
            user = store(self.model, userData)
            data['user_id'] = user.id
            data['status'] = 'pending'
            profile = store(models.school_profile, data)
        except Exception as e:
            app.logger.debug(e)
            return failed(str(e))
        return success()
