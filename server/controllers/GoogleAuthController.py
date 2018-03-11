import json
from flask import current_app as app, request
import models
from utils import request_json, get_https_conn, success, failed

class GoogleAuthController():
    model = models.user
    def login(arg):
        data = request_json()
        token = data.get('token', None)
        if not token:
            return failed('Token is required')
        try:
            # params = urllib.parse.urlencode({'secret': app.config['recaptcha_secretkey'], 'response': token})
            # headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
            conn = get_https_conn('www.googleapis.com')
            conn.request('GET', '/oauth2/v3/tokeninfo?id_token=%s'%(token))
            data2 = conn.getresponse().read().decode('utf8')
        except Exception as e:
            raise e
        finally:
            conn.close()
        data2 = json.loads(data2)
        print(data2)
        return success()
        # result
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

        # conn.close()
        #
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
