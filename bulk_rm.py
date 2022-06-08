import subprocess as sp

"""
subprocess 에서 출력되는 결과값을 문자열 데이터로 사용하고 싶은 경우 check_output 함수를 사용한다.
out = subprocess.check_output (['ls', '-al'] )

Popen 은 subprocess 모듈에서 사용되는 대부분의 함수 실행에 실질적으로 관여하는 함수이며, 다양한 옵션들을 통해 call, check_output 등 보다 유연하게 사용할 수 있다.

>>> proc = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE, stderr=subprocess.PIPE )
>>> out = proc.communicate()
"""


def bulk_rm(rm_bulk_data, rm_path):
    """
    Type == String |  split 함수 실행
    """
    prefix = input('common prefix')
    postfix = input('common postfix')

    # to Array
    if type(rm_bulk_data) is str:
        will_removes = rm_bulk_data.split()
    elif type(rm_bulk_data) is list:
        pass

    for i in will_removes:
        cmd = ['rm', rm_path + prefix + i + postfix]
        out = sp.run(cmd)
        if out.returncode != 0:
            print('fail', cmd)
