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

class AuthController(ResourceController):
    model = models.user
    def register(self):
        data = request_json()
        # recaptcha
        errorMsg = validate_recaptcha(data['recaptcha'])
        if errorMsg:
            return failed(errorMsg)
        #
        schema = {
            'email': rules['email'],
            'first_name': {'required': True, 'type': 'string', 'maxlength': 255},
            'last_name': {'required': True, 'type': 'string', 'maxlength': 255},
            'password': rules['password'],
            'user_type': {'required': True, 'type': 'string', 'allowed': ['school', 'student']},
        }
        v = make_validator(schema)
        if not v.validate(data):
            return failed('Invalid input', {'error': v.errors})
        if data.get('user_type') != 'student':
            return failed('Invalid user_type')
        user = self.model.objects.filter(email=data['email']).first()
        if user:
            return failed('An account with this email already exists')
        data['password'] = hash_pwd(data['password'])
        try:
            user = store(self.model, data)
            profileData = dict_pluck(data, ['first_name', 'last_name'])
            profileData['user_id'] = user.id
            profile = store(models.student_profile, profileData)
            self.do_send_confirmation_email(user.email, user.id)
        except Exception as e:
            print(e)
            errorMsg = str(e)
        if errorMsg:
            return failed(errorMsg)
        login_user(user)
        return success()
    def login(self):
        data = request_json()
        # recaptcha
        errorMsg = validate_recaptcha(data['recaptcha'])
        if errorMsg:
            return failed(errorMsg)
        user = self.model.objects.filter(email=data['email']).first()
        if user.user_type != data['user_type']:
            user = None
        if not user:
            return failed('User not found')
        if not pwd_hashed_compare(data['password'], user.password):
            return failed('Incorrect password')
        login_user(user, remember = data.get('remember'))
        return success()
    def logout(self):
        logout_user()
        return success()
    def current_user(self):
        item = {}
        if current_user.is_authenticated:
            item = user_to_dict(current_user)
        else:
            item['is_anonymous'] = True
        return success(item)
    # confirm email
    def confirm_email(self):
        data = request_json()
        token = data.get('token', None)
        user = current_user
        errorMsg = None
        if user.email_confirmed:
            errorMsg = 'Your email already be confirmed'
        if token:
            item = models.confirmation_email.objects().filter(token = token).first()
            if not item or item.email != user.email:
                errorMsg = 'Illegal request'
            else:
                expired = (datetime.now() - item.updated_at).seconds > 3600 * 1
                if expired:
                    errorMsg = 'Link expired'
                else:
                    user.email_confirmed = True
                    user.save()
                    item.delete()
        else:
            errorMsg = 'Token is required'
        return failed(errorMsg) if errorMsg else success()
    #
    def send_confirmation_email(self):
        data = request_json()
        # recaptcha
        errorMsg = validate_recaptcha(data['recaptcha'])
        if errorMsg:
            return failed(errorMsg)
        #
        errorMsg = None
        try:
            self.do_send_confirmation_email(data['email'], current_user.id)
        except Exception as e:
            print(e)
            errorMsg = str(e)
        return failed(errorMsg) if errorMsg else success()
    def update_email(self):
        data = request_json()
        schema = {
            'email': rules['email'],
        }
        v = make_validator(schema)
        if not v.validate(data):
            return failed('Invalid input', {'error': v.errors})
        current_user.email = data['email']
        current_user.email_confirmed = False
        current_user.save()
        return success()
    # forgot password
    def send_reset_password_email(self):
        data = request_json()
        # recaptcha
        errorMsg = validate_recaptcha(data['recaptcha'])
        if errorMsg:
            return failed(errorMsg)
        # validate
        schema = {
            'email': rules['email'],
        }
        v = make_validator(schema)
        if not v.validate(data):
            return failed('Invalid input', {'error': v.errors})
        # whether exist
        email = data['email']
        user = self.model.objects.filter(email = email).first()
        if not user:
            return failed('The account for the given email does not exist')
        if user.user_type == 'school' and get_user_profile(user).status != 'normal':
            return failed('This account is currently not enabled')
        #
        data = {
            'token': md5(str_rand(16)),
            'email': email,
        }
        record = models.reset_password_email.objects.filter(email=email).first()
        if record:
            item = update(models.reset_password_email, data, record.id)
        else:
            item = store(models.reset_password_email, data)
        link = url_for('index', _external = True) + 'reset-password?token=' + data['token'] # generate absolute link
        print('reset password link:', link)
        try:
            msg = Message('[%s] Reset your account password'%(app.config['site_name']), recipients=[email])
            msg.html = render_template('email/reset-password.html', email = email, link = link, app = app)
            mail.send(msg)
        except Exception as e:
            return failed(str(e))
        return success()
    def check_reset_password_token(self):
        data = request_json()
        # recaptcha
        errorMsg = validate_recaptcha(data['recaptcha'])
        if errorMsg:
            return failed(errorMsg)
        token = data.get('token', None)
        if not token:
            return failed('Illegal request')
        item = models.reset_password_email.objects.filter(token=token).first()
        if not item:
            return failed('No record found with given token')
        expired = (datetime.now() - item.updated_at).seconds > 3600 * 1
        if expired:
            return failed('Link expired')
        user = self.model.objects.filter(email=item.email).first()
        return success(user_to_dict(user))
    def reset_password(self):
        data = request_json()
        # recaptcha
        errorMsg = validate_recaptcha(data['recaptcha'])
        if errorMsg:
            return failed(errorMsg)
        # validate
        schema = {
            'user_id': {'required': True, 'type': 'string'},
            'token': {'required': True, 'type': 'string'},
            'password': rules['password'],
        }
        v = make_validator(schema)
        if not v.validate(data):
            return failed('Invalid input', {'error': v.errors})
        #
        record = models.reset_password_email.objects.filter(token=data['token']).first()
        user = self.model.objects.filter(id = data['user_id']).first()
        if not record or not user or record.email != user.email:
            return failed('Illegal request')
        #
        expired = (datetime.now() - record.updated_at).seconds > 3600 * 1
        if expired:
            return failed('Link expired')
        user.password = hash_pwd(data['password'])
        user.email_confirmed = True
        user.save()
        record.delete()
        return success()
    # private
    def do_send_confirmation_email(self, email, userId):
        data = {
            'user_id': userId,
            'token': md5(str_rand(16)),
            'email': email,
        }
        record = models.confirmation_email.objects.filter(user_id=userId).first()
        if record:
            item = update(models.confirmation_email, data, record.id)
        else:
            item = store(models.confirmation_email, data)
        # generate absolute link
        link = url_for('index', _external = True) + 'confirm-email?token=' + data['token']
        print('confirm email link:', link)
        msg = Message('[%s] Confirm Email Address'%(app.config['site_name']), recipients=[email])
        msg.html = render_template('email/confirm-email.html', email = email, link = link)
        mail.send(msg)
        return item

class UserController(AuthController):
    def profile(self):
        data = (request_json() or {}).get('data')
        if not data:
            # get
            return success(to_dict(get_user_profile(current_user)))
        else:
            # update
            if current_user.user_type == 'student':
                # validate
                schema = {
                    'avatar': {'required': True, 'type': 'string', 'maxlength': 255},
                    'first_name': {'required': True, 'type': 'string', 'maxlength': 255},
                    'last_name': {'required': True, 'type': 'string', 'maxlength': 255},
                    'gender': rules['gender'],
                    'birthday': {'required': True, 'type': 'number'},
                    'nationality': {'required': True, 'type': 'string', 'maxlength': 255},
                    'country_of_residence': {'required': True, 'type': 'string', 'maxlength': 255},
                    'email': rules['email'],
                    'phone': {'required': True, 'type': 'string', 'maxlength': 255},
                    'passport_info': {'required': True, 'maxlength': 1000},
                    'emergency_contact_persons': {'required': True, 'maxlength': 1000},
                }
                v = make_validator(schema)
                if not v.validate(data):
                    return failed('Invalid input', {'error': v.errors})
                try:
                    t = data['passport_info']
                    if not keys_match(t, ['number', 'issued_country', 'expiry_date']):
                        return failed('Invalid input')
                    for k, v in t.items():
                        if not v:
                            return failed('The %s is required.'%(k.replace('_', ' ')))
                    t = data['emergency_contact_persons']
                    keys = ['name', 'relationship', 'tel']
                    if not keys_match(t[0], keys) or not keys_match(t[1], keys):
                        return failed('Invalid input')
                    for k, v in t[0].items():
                        if not v:
                            return failed('The %s is required.'%(k.replace('_', ' ')))
                except Exception as e:
                    print(e)
                    return failed('Invalid input')
            # todo validate school profile
            #
            model = models.student_profile if current_user.user_type == 'student' else models.school_profile
            profile = get_user_profile(current_user)
            if current_user.email != data['email']:
                current_user.email = data['email']
                current_user.email_confirmed = False
                current_user.save()
            update(model, data, profile.id)
            return success()
