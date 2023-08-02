
import os


def return_datas():
    """
    편의성을 위해 사용될 데이터들을 사전에 기입 하는 곳
    return datas = {
        path, yaml, json, raw_data
    }
    """
    datas = {}
    datas['path'] = '/data/fitzme-data/tmp/'
    datas['yaml'] = ""
    datas['json'] = ""
    datas['raw_datas'] = """ 
        34880810-f88c-5f01-ae8e-839ec80827f0
        3bfe7750-956d-5d62-b5c9-fc8cdfa75170
        1e63d5a5-51e9-5f1e-8874-89f2578d314d
        87389227-d86c-5f40-83dd-27aa5a06b32a
        0bb0c38a-d116-5b46-b0ae-adfce010a64c
        ef25f7dc-3b64-53ac-b739-ecaf9cad3303
        2f025812-7492-54ce-9ff4-f6303d9b94ba
        df55fcad-0a04-5d69-9956-ca6225defd0f
        64c4c8dc-bc0c-5ca8-a68a-905cd94d73d9
        a054af3b-8b8f-56e1-9845-7ef5610d0e8f
        88ed02d3-4c59-5508-9564-7a44435b75a8
        4c193efb-84b2-5279-9101-bb86073b3bd6
        1cc2733b-1aac-5271-ad6b-afa4ee08cacd
        6c48f6df-19be-51c5-b192-151873a08077
        97f79793-daa7-59e1-8b70-e4914381a1e8
        609c4272-beb6-5d1b-bb3e-e4ab781d8fcf
    """
    return datas


PROCESSOR_CONFIG = {
    # 크롤링 아이템(data, image 등)이 있는 폴더 경로
    'input_path': os.path.expanduser('~/tmp/20-04-27_20-05-08/'),

    # 결과물이 저장될 폴더 경로
    'output_path': os.path.expanduser('/data/fitzme-data/tmp/'),

    # JWT token을 받기 위한 FIZME 서비스 계정의 email, 비밀번호
    'email': 'intern@intellisys.co.kr',
    'password': 'qwer1234!',

    # 서비스 import 시 참고할 fitzme-crawling repo 경로
    'mapping': os.path.expanduser('~/fitzme-crawling/'),
}
