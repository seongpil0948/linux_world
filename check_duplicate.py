import json
from re import compile
from os import path, listdir
import numpy as np

result_path = path.expanduser("~/fashion-crawling-data/")
p = compile('\d{1,2}_\w+')

all_brands = list(filter(lambda x: p.match(
    x) is not None, listdir(result_path)))
brandNums = map(lambda b: b.split("_")[0], all_brands)

mappings = {num: [brand] for num, brand in zip(brandNums, all_brands)}
mappings['all'] = all_brands
msg = ''
for k, v in mappings.items():
    msg += f"{k}: {v}\n"
select = input(f"Please Input 'Crawler Number' Or 'all' \n{msg}")
brand = mappings[select][0]

CTGR_MADE_IDX = -1
brand_path = path.join(result_path, brand)

# log.json: items by category
with open(path.join(brand_path, 'log.json')) as f:
    all_cates = json.load(f)
others = all_cates[:-1]
target = all_cates[CTGR_MADE_IDX]
ctgr_codes = set(target['items_present'])

# duplicate, not duplicate
d = []
nd = set()

for ctgr in others:
    # current category item list
    codes = ctgr['items_present']
    # num of codes of category
    d += codes
    for code in codes:
        nd.add(code)

print(f"""
    target info: \n 
    items length: {len(ctgr_codes)} \n
    name: {target['cat_list']} \n
    url: {target['page_url']}
""")
print(f"""
\n\n is duplicate category?
   duplicate length: {nd.intersection(ctgr_codes)} \n
   not duplicate codes {ctgr_codes - nd}

""")


# d = np.unique(b, return_counts=True)
# for code, count in zip(d):
#     if count > 1:
