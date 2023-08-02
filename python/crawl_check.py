import os
a = os.listdir('./')

print(f"Num Of Images: {len(a)}")
ids = set()
ds = 0
ts = 0
anonymous = []
for i in a:
    [item_id, detail_or_title, _] = i.split('_')
    ids.add(item_id)
    if detail_or_title == 'd':
        ds += 1
    elif detail_or_title == 't':
        ts += 1
    else:
        anonymous.append(i)

print(
    f"Num Of datas: {len(ids)} \n Num of detail Images: {ds} \n Num of Title Imgs: {ts} ")

avg_ds = ds // len(ids)
avg_ts = ts // len(ids)

print(f"Avg Detail Imgs: {avg_ds} \n Avg Title Imgs: {avg_ts}")

if len(anonymous) > 0:
    print("anonymous: ", anonymous)
