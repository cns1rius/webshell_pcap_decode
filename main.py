# @Author: s1rius
# @Date: 2023-08-16 11:36:42
# @LastEditTime: 2023-08-16 11:39:03
# @Description: https://s1rius.space/

import os
import sys
import godzilla
import behinder


def is_Godzilla():
    if (
        r"=eval%28base64_decode%28strrev%28urldecode%28%27"  # 按照Eval_Xor_Base64来写的 后续会在此处增加规则 或在tshark出增加筛选
        in open("request_data.txt").readlines()[1]
    ):
        return True


def is_Antsword():
    return False


def is_Behinder():
    return False


if __name__ == "__main__":
    filename = sys.argv[1]
    os.system(
        f'tshark -r {filename} -T fields -Y "http.request.method == POST" -e http.file_data > request_data.txt'
    )
    os.system(
        f'tshark -r {filename} -T fields -Y "http.response.code==200" -e http.file_data > response_data.txt'
    )
    if is_Godzilla():  # 后续如有混淆 可在此处调整优先级
        print("[*] Using Godzilla")
        godzilla = godzilla.Godzilla()
        godzilla.decode_All()
    elif is_Antsword():
        pass
    elif is_Behinder():
        behinder = behinder.Behinder()
        behinder.decode_All()
    else:
        print("[-] Unsupported webshell manager")
