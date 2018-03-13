import json
from flask import current_app as app, request, session
from flask_login import login_user, current_user
import models
from utils import request_json, get_https_conn, success, failed, user_to_dict, sort_models

# google api result
# {
#    'at_hash':'jlovz6l6rXo-Rjom8Rf0YQ',
#    'aud':'395826608446-1npm72l9egmcolbqpvqlatjjegr9ibnj.apps.googleusercontent.com',
#    'picture':'https://lh5.googleusercontent.com/-t122b6zQO-A/AAAAAAAAAAI/AAAAAAAAAnk/Wg34ESxoxQs/s96-c/photo.jpg',
#    'iss':'accounts.google.com',
#    'family_name':'He',
#    'email_verified':'true',
#    'kid':'ac2b63faefcf8362f4c528e7c78433879387016b',
#    'given_name':'Xinxin',
#    'name':'Xinxin He',
#    'alg':'RS256',
#    'sub':'111984417102465607133',
#    'jti':'d323fe2ed21e090db8c06007df81095d35ac9e6c',
#    'exp':'1520770257',
#    'locale':'zh-CN',
#    'email':'phphe@outlook.com',
#    'azp':'395826608446-1npm72l9egmcolbqpvqlatjjegr9ibnj.apps.googleusercontent.com',
#    'iat':'1520766657'
# }
#
# official example
# try:
#     # Specify the CLIENT_ID of the app that accesses the backend:
#     idinfo = id_token.verify_oauth2_token(, requests.Request(), app.config['google_singin_client_id'])
#     print(idinfo)
#
#     # Or, if multiple clients access the backend server:
#     # idinfo = id_token.verify_oauth2_token(token, requests.Request())
#     # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
#     #     raise ValueError('Could not verify audience.')
#
#     if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
#         raise ValueError('Wrong issuer.')
#
#     # If auth request is from a G Suite domain:
#     # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
#     #     raise ValueError('Wrong hosted domain.')
#
#     # ID token is valid. Get the user's Google Account ID from the decoded token.
#     userid = idinfo['sub']
# except ValueError:
#     # Invalid token
#     pass
#
class GoogleAuthController():
    model = models.user
    def login(self):
        data = request_json()
        token = data.get('token', None)
        if not token:
            return failed('Token is required')
        try:
            conn = get_https_conn('www.googleapis.com')
            conn.request('GET', '/oauth2/v3/tokeninfo?id_token=%s'%(token))
            respData = conn.getresponse().read().decode('utf8')
        except Exception as e:
            raise e
        finally:
            conn.close()
        info = json.loads(respData)
        if info.get('error_description'):
            return failed(info['error_description'])
        if info['aud'] not in [app.config['google_singin_client_id']]:
            return failed('Could not verify audience.')
        if info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return failed('Wrong issuer.')
        # this is rare
        if not info['email_verified']:
            return failed('Your google email not verified.')
        gid = info['sub']
        user = self.model.objects.filter(google_id=gid).first()
        if user:
            login_user(user)
            return success(data={'linked':True})
        possibleUsers = sort_models(self.model.objects.filter(email=info['email'])[:])
        session['google_user_info'] = info
        return success(data={'linked':False, 'possible_users': [user_to_dict(v) for v in possibleUsers]})
    def link(self):
        data = request_json()
        info = session.get('google_user_info')
        if not info:
            return failed('Illegal request')
        user = current_user
        uid = data.get('user_id')
        if uid:
            user = self.model.objects.filter(id=uid).first()
            if not user:
                return failed('User not found with given id')
            if user.email != info['email']:
                return failed('Illegal request')
            possibleUsers = self.model.objects.filter(email=user.email)
            # other users with same email may be fake
            for value in possibleUsers:
                if value.id != user.id:
                    if value.email_confirmed:
                        value.email_confirmed = False
                        value.save()
            login_user(user)
        gid = info['sub']
        user.google_id = gid
        if user.email == info['email']:
            user.email_confirmed = True
        user.save()
        return success()
