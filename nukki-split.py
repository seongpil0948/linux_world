import os


split_imgs = set()
split_path = os.path.expanduser('~/tmp/test_split')
for d in os.listdir(split_path):
    for f in os.listdir(os.path.join(split_path, d)):
        file_name = os.path.splitext(f)[0]
        idx_end = file_name.find('_', 3)
        brand = file_name[:idx_end]
        idx_start = idx_end + 1
        idx_end = file_name.find('_', idx_start)
        item_code = file_name[idx_start:idx_end]
        split_imgs.add(item_code)

nukkis = set()
nukki_path = os.path.expanduser('~/tmp/20-05-09_20-05-15/nukki_image')
for d in os.listdir(split_path):
    for f in os.listdir(os.path.join(split_path, d)):
        file_name = os.path.splitext(f)[0]
        idx_end = file_name.find('_', 3)
        brand = file_name[:idx_end]
        idx_start = idx_end + 1
        idx_end = file_name.find('_', idx_start)
        item_code = file_name[idx_start:idx_end]
        nukkis.add(item_code)
print(len(split_imgs))
print(len(nukkis))
print(split_imgs == nukkis)
