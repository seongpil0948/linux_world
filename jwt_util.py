import jwt
import datetime
import requests
from config import *


def get_jwt_token():
    url_login = "https://fitzme-gateway-jx-staging.fitzme.xyz/mobile/v1/login/"

    data = {
        'email': PROCESSOR_CONFIG['email'],
        'password': PROCESSOR_CONFIG['password']
    }

    try:
        response = requests.post(url_login, json=data)
        if not response.ok:
            print(
                f'Login fail (return code: {response.status_code}, message: {response.text})')
            exit()
    except requests.exceptions.RequestException as e:
        print(f'Login fail (detail: {e})')
        exit()

    jwt_token = response.json()['token']
    jwt_decoded = jwt.decode(jwt_token, verify=False)
    jwt_decoded['expire'] = datetime.datetime.fromtimestamp(jwt_decoded['exp'])

    print(f'Info: JWT token - {jwt_token} / {jwt_decoded}')

    return (jwt_token, jwt_decoded)


def token_refresh(jwt_token):
    url_refresh = "https://fitzme-gateway-jx-staging.fitzme.xyz/mobile/v1/token_refresh/"

    data = {
        'token': jwt_token
    }

    try:
        response = requests.post(url_refresh, json=data)
        if not response.ok:
            print(
                f'Refresh fail (return code: {response.status_code}, message: {response.text})')
            exit()
    except requests.exceptions.RequestException as e:
        print(f'Refresh fail (detail: {e})')
        exit()

    jwt_token = response.json()['token']
    jwt_decoded = jwt.decode(jwt_token, verify=False)
    jwt_decoded['expire'] = datetime.datetime.fromtimestamp(jwt_decoded['exp'])

    print(f'Info: JWT token refreshed - {jwt_token} / {jwt_decoded}')
    return (jwt_token, jwt_decoded)
