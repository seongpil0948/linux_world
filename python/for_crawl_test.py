from helper.cat_reader import read_categories_yaml
from helper.jwt_util import get_data_brand
import os
import sys
path = os.path.expanduser('~/fitzme-crawling/')
sys.path.append(os.path.join(path))


data = get_data_brand()
shops = set([shop['name'] for shop in data])
ls = os.listdir(path)
targets = [t for t in ls if t in shops]

for t in targets:
    ver, cates = read_categories_yaml(os.path.join(path, t, 'categories.yaml'))
    print(cates[0])
    break
