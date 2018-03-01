from flask import current_app as app, request, render_template, url_for, redirect
import models
from ResourceController import ResourceController, store, update
from utils import failed, success, make_validator, hash_pwd, pwd_hashed_compare, dict_pluck, request_json, to_dict, validate_recaptcha, str_rand, user_to_dict, render_spa
from flask_login import login_user, logout_user, current_user
from mail import mail
from flask_mail import Message
from datetime import datetime

class UserController(ResourceController):
    model = models.user
    def register(self):
        data = request_json()
        # recaptcha
        vdt = validate_recaptcha(data['recaptcha'])
        if not vdt['success']:
            return failed('Recaptcha failed: ' + ', '.join(vdt['error-codes']))
        #
        schema = {
            'email': {'required': True, 'type': 'string', 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', 'maxlength': 255},
            'first_name': {'required': True, 'type': 'string', 'maxlength': 255},
            'last_name': {'required': True, 'type': 'string', 'maxlength': 255},
            'password': {'required': True, 'type': 'string', 'maxlength': 255},
            'user_type': {'required': True, 'type': 'string', 'allowed': ['school', 'student']},
        }
        v = make_validator(schema)
        if not v.validate(data):
            return failed('Invalid input', {'error': v.errors})
        if data.get('user_type') != 'student':
            return failed('Invalid user_type')
        if self.model.objects.filter(email=data['email'], email_confirmed=True).first():
            return failed('Email already exists')
        data['password'] = hash_pwd(data['password'])
        try:
            user = store(self.model, data)
            profileData = dict_pluck(data, ['first_name', 'last_name'])
            profileData['user_id'] = user.id
            profile = store(models.student_profile, profileData)
            self.do_send_activation_email(user.email, user.id)
        except Exception as e:
            print(e)
            errorMsg = str(e)
        if 'errorMsg' in locals():
            return failed(errorMsg)
        return success('', {'id': str(user.id)})
    def login(self):
        data = request_json()
        # recaptcha
        vdt = validate_recaptcha(data['recaptcha'])
        if not vdt['success']:
            return failed('Recaptcha failed: ' + ', '.join(vdt['error-codes']))
        #
        item = models.user.objects.filter(email=data['email']).first()
        if not item:
            return failed('User not found')
        if not pwd_hashed_compare(data['password'], item.password):
            return failed('Incorrect password')
        login_user(item, remember = data.get('remember'))
        return success('', {'data': user_to_dict(item)})
    def logout(self):
        logout_user()
        return success()
    def current_user(self):
        item = {}
        if current_user.is_authenticated:
            item = user_to_dict(current_user)
        else:
            item['is_anonymous'] = True
        return success('', {'data': item})
    # active email
    def active_email(self):
        token = request.args.get('token')
        if token:
            item = models.active_email.objects().filter(token = token).first()
            if not item:
                errorMsg = 'Illegal request'
            else:
                expired = (datetime.now() - item.updated_at).seconds > 3600 * 1
                user = models.user.objects().filter(id = item.user_id).first()
                if expired or user.email != item.email:
                    errorMsg = 'Link expired'
                elif models.user.objects().filter(email = item.email, email_confirmed = True).first():
                    errorMsg = 'Email already exists'
                else:
                    user.email_confirmed = True
                    user.save()
                    item.delete()
            if errorMsg:
                return redirect(url_for('activeEmail'), error = errorMsg)
        return render_spa('spa.html')
    def send_activation_email(self):
        data = request_json()
        # recaptcha
        vdt = validate_recaptcha(data['recaptcha'])
        if not vdt['success']:
            return failed('Recaptcha failed: ' + ', '.join(vdt['error-codes']))
        #
        errorMsg = None
        try:
            self.do_send_activation_email(data['email'], current_user.id)
        except Exception as e:
            print(e)
            errorMsg = str(e)
        return failed(errorMsg) if errorMsg else success()
    # forgot password
    def forgot_password(self):
        item = {}
        if current_user.is_authenticated:
            item = user_to_dict(current_user)
        else:
            item['is_anonymous'] = True
        return success('', {'data': item})
    # private
    def do_send_activation_email(self, email, userId):
        data = {
            'user_id': userId,
            'token': str_rand(16),
            'email': email,
        }
        if models.activation_email.objects.filter(user_id=userId).first():
            item = update(models.activation_email, data)
        else:
            item = store(models.activation_email, data)
        link = url_for('activeEmail', token = data['token'])
        msg = Message("Confirm Email Address", recipients=[email])
        msg.html = render_template('email/active-email.html', email = email, link = link)
        mail.send(msg)
        return item
