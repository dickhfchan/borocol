from flask import current_app as app, request, render_template, url_for, redirect
import models
from plugins.ResourceController import ResourceController, store, update
from utils import failed, success, make_validator, hash_pwd, pwd_hashed_compare
from utils import dict_pluck, request_json, to_dict, sort_models, validate_recaptcha
from utils import str_rand, user_to_dict, md5
from flask_login import login_user, logout_user, current_user
from plugins.mail import mail
from flask_mail import Message
from datetime import datetime

class UserController(ResourceController):
    model = models.user
    emailSchema = {'required': True, 'type': 'string', 'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', 'maxlength': 255}
    passwordSchema = {'required': True, 'type': 'string', 'maxlength': 255}
    def register(self):
        data = request_json()
        # recaptcha
        errorMsg = validate_recaptcha(data['recaptcha'])
        if errorMsg:
            return failed(errorMsg)
        #
        schema = {
            'email': self.emailSchema,
            'first_name': {'required': True, 'type': 'string', 'maxlength': 255},
            'last_name': {'required': True, 'type': 'string', 'maxlength': 255},
            'password': self.passwordSchema,
            'user_type': {'required': True, 'type': 'string', 'allowed': ['school', 'student']},
        }
        v = make_validator(schema)
        if not v.validate(data):
            return failed('Invalid input', {'error': v.errors})
        if data.get('user_type') != 'student':
            return failed('Invalid user_type')
        q = self.model.objects.filter(email=data['email'])
        isEmailTaken = any(v.email_confirmed for v in q[:])
        if isEmailTaken:
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
        if errorMsg:
            return failed(errorMsg)
        login_user(user)
        return success('', {'id': str(user.id)})
    def login(self):
        data = request_json()
        # recaptcha
        errorMsg = validate_recaptcha(data['recaptcha'])
        if errorMsg:
            return failed(errorMsg)
        possibleUsers = self.model.objects.filter(email=data['email'])[:]
        possibleUsers = sorted(possibleUsers, key = lambda v: int(v.email_confirmed), reverse=True ) # put email_confirmed users on the top
        if len(possibleUsers) == 0:
            return failed('User not found')
        user = next((item for item in possibleUsers if pwd_hashed_compare(data['password'], item.password)), None) # find first matched user
        if not user:
            return failed('Incorrect password')
        login_user(user, remember = data.get('remember'))
        return success('', {'data': user_to_dict(user)})
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
        data = request_json()
        token = data.get('token', None)
        user = current_user
        errorMsg = None
        if user.email_confirmed:
            errorMsg = 'Your email already active'
        if token:
            item = models.activation_email.objects().filter(token = token).first()
            if not item or item.email != user.email:
                errorMsg = 'Illegal request'
            else:
                expired = (datetime.now() - item.updated_at).seconds > 3600 * 1
                if expired:
                    errorMsg = 'Link expired'
                elif any(v.email_confirmed for v in self.model.objects().filter(email = item.email)):
                    errorMsg = 'Email already exists'
                else:
                    user.email_confirmed = True
                    user.save()
                    item.delete()
        else:
            errorMsg = 'Token is required'
        return failed(errorMsg) if errorMsg else success()
    #
    def send_activation_email(self):
        data = request_json()
        # recaptcha
        errorMsg = validate_recaptcha(data['recaptcha'])
        if errorMsg:
            return failed(errorMsg)
        #
        errorMsg = None
        try:
            self.do_send_activation_email(data['email'], current_user.id)
        except Exception as e:
            print(e)
            errorMsg = str(e)
        return failed(errorMsg) if errorMsg else success()
    def update_email(self):
        data = request_json()
        schema = {
            'email': self.emailSchema,
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
            'email': self.emailSchema,
        }
        v = make_validator(schema)
        if not v.validate(data):
            return failed('Invalid input', {'error': v.errors})
        # whether exist
        email = data['email']
        if self.model.objects.filter(email = email).count() == 0:
            return failed('The account for the given email does not exist')
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
        link = url_for('resetPassword', token = data['token'], _external = True) # generate absolute link
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
        # return possible users
        possibleUsers = ort_models(self.model.objects.filter(email=item.email)[:])
        return success(data = {'data': [user_to_dict(v) for v in possibleUsers]})
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
            'password': self.passwordSchema,
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
        # other users may used wrong email
        for item in self.model.objects.filter(email = user.email):
            item.email_confirmed = False
            item.save()
        user.password = hash_pwd(data['password'])
        user.email_confirmed = True
        user.save()
        record.delete()
        return success()
    # private
    def do_send_activation_email(self, email, userId):
        data = {
            'user_id': userId,
            'token': md5(str_rand(16)),
            'email': email,
        }
        record = models.activation_email.objects.filter(user_id=userId).first()
        if record:
            item = update(models.activation_email, data, record.id)
        else:
            item = store(models.activation_email, data)
        # generate absolute link
        link = url_for('activeEmail', token = data['token'], _external = True)
        print('active email link:', link)
        msg = Message('[%s] Confirm Email Address'%(app.config['site_name']), recipients=[email])
        msg.html = render_template('email/active-email.html', email = email, link = link)
        mail.send(msg)
        return item
