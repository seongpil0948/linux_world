SEND_JSON_PATH="json/asset/send.json"
DEFINED_JSON_PATH="json/asset/defined.json"

# 교집합과 각 집합에만 존재하는 요소들을 예쁘게 print 하는 python code 작성
# Create Python codes that beautifully print intersections and elements that exist only in each set
# only compare with json keys

import json
from pprint import pprint
def get_json(path):
    with open(path, 'r') as f:
        return json.load(f)
  

def get_diff(a, b):
    a_set = set(a.keys())
    b_set = set(b.keys())
    a_b_intersection = a_set.intersection(b_set)
    a_b_difference = a_set.difference(b_set)
    b_a_difference = b_set.difference(a_set)
    return a_b_intersection, a_b_difference, b_a_difference


def print_diff(a, b):
    a_b_intersection, a_b_difference, b_a_difference = get_diff(a, b)
    print(">>>>>> Intersection: >>>>>>")
    pprint(a_b_intersection)
    print("\n\n===> Only in a: ")
    pprint(a_b_difference)
    print("\n\n===> Only in b: ")
    pprint(b_a_difference)
    pprint("<<<<<< Intersection: <<<<<<")

if __name__ == '__main__':
    a = get_json(SEND_JSON_PATH)
    b = get_json(DEFINED_JSON_PATH)
    print_diff(a, b)