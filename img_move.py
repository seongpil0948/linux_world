import os
import json
import shutil
import pprint
# from is_verified_preprocessed import datas

# uuids = list(map(lambda x: x['uuid'], datas()))
# print('target uuids =>', len(uuids))

origin_imgs_path = '/data/fitzme-data/tmp/'  # nexus
# to_be_moved = '/data/hollimSsi/img/'

origin_imgs = os.listdir(origin_imgs_path)


"""
# 넥서스 이미지로 부터 조건에 맞는 UUID에 해당하는 이미지들을 불러와 settle_imgs 에 저장
for img in origin_imgs:
    for uuid in uuids:
        if 'title' in img:
            if uuid == os.path.splitext(img)[0].replace('-title', ''):
                file = os.path.join(origin_imgs_path, img)
                shutil.copy2(file, os.path.join(to_be_moved, img))
                break
        else:
            if uuid == os.path.splitext(img)[0]:
                file = os.path.join(origin_imgs_path, img)
                shutil.copy2(file, os.path.join(to_be_moved, img))
                break
"""


"""
누끼 이미지가 key, 타이틀 이미지가 value인 imgs dictionary를 제작
no_title_uuids = []
imgs = {}
for i in settle_imgs:
    if '-title' not in i:
        imgs[i] = None

for j in settle_imgs:
    if '-title' in j:
        imgs[j[:j.rfind('-')] + '.png'] = j

# imgs 의 value 가 None 인 uuid 추출 json 파일로 저장
for z in imgs:
    if imgs[z] is None:
        no_title_uuids.append(os.path.splitext(z)[0])
print('no_title_uuids ==>', no_title_uuids)

with open('no_title_uuids.json', 'w') as f:
    json.dump(no_title_uuids, f, indent=4)
"""
