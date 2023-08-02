import pprint
import os
import sys
import json
import requests
from pprint import pprint
# import skimage.io
import re
from time import sleep
import datetime
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

try:
    from . import jwt_util
except:
    import jwt_util
# from config import *

# uuids= [
# "99f99d48-014f-51b4-938b-f4b4cc99a49f",
# "e0912048-caf7-5d48-953b-8afde780e555"
# ]
# for i in uuids:
#     print(i)
#     image = skimage.io.imread(str(f'/data/fitzme-data/tmp/{i}.png'))
#     print(image)


# url = f"http://fitzme-service.jx-staging.svc.cluster.local/qa/v1/sample_garment/?brand=32_Frombeginning&qa_round=20-04-01_20-04-15"
# url = f"http://fitzme-service.jx-staging.svc.cluster.local/qa/v1/sample_garment/?brand=32_Frombeginning"
jwt_token, jwt_decoded = jwt_util.get_jwt_token()

if (datetime.datetime.now() > jwt_decoded['expire']):
    jwt_token, jwt_decoded = jwt_util.token_refresh(jwt_token)


" get Data"
# def adjust(m):
# return f"={m.group()}"
# res = requests.get(url, headers={'Authorization': f'JWT {jwt_token}'}).json()
# params = {}
# add = {}
# items = []
# for i in res:
#     if '=' not in i['url']:
#         params[i['uuid']] =  { 'url': re.sub('\d', adjust, i['url'], 1)}

# pprint.pprint(params)
# print(len(params))

# "Patch Data"
# count = 0
# for uuid, param in params.items():
#     # print(uuid, param)
patch_url = f'http://fitzme-service.jx-staging.svc.cluster.local/qa/v1/sample_garment/1aaf7a26-a5d2-5546-9f04-9bbf37525943/'
response = requests.patch(url=patch_url, json={'is_deploy': False}, headers={
                          'Authorization': f'JWT {jwt_token}'})
if not response.ok:
    print(f'Import fail (return code: {response.status_code})')
#     count += 1
#     sleep(0.2)
# print('2 ===>', count)
