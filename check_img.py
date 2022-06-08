import requests as r

urls = [
    'https://www.google.com/search?q=%EA%B3%B0%ED%86%A0%ED%86%A0&sxsrf=ALeKk03ou6N8yjyeViKAsFmpub1aJEGYvQ:1616335506554&tbm=isch&source=iu&ictx=1&fir=ac6eOvhrB5IJDM%252C4KBxLy8AB-24YM%252C_&vet=1&usg=AI4_-kT_GA93kpPp48LtqMYxzmXPiBg_yg&sa=X&ved=2ahUKEwj9tdL9xsHvAhVME6YKHUOjDlMQ9QF6BAgdEAE#imgrc=ac6eOvhrB5IJDM',
    'http://img.bechic.co.kr/17Hk9w6EMi',
    'https://common-unique.com/date/2020/0921/3/8o-re-re-intro-190109_01.jpg',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ46ionOgM9mLtcwMtRqbXc4OkwnNAnCqrZZw&usqp=CAU'
]

rs = [r.get(url) for url in urls]


def valid_img_filter(response):
    r = response
    c_type = r.headers.get('Content-Type')
    code = r.status_code
    if code == 200 and c_type.startswith("image"):
        return True
    print(
        f"Invalid Image URL: {r.url} \n Content Type: {c_type} \n Encoding: {r.encoding} ")
    return False


valid_rs = list(filter(valid_img_filter, rs))
assert len(valid_rs) == len(urls)
