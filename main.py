# @Author: s1rius
# @Date: 2023-08-16 11:36:42
# @LastEditTime: 2023-08-16 11:39:03
# @Description: https://s1rius.space/

import os
import sys
import godzilla


def is_Godzilla():
    return True


if __name__ == "__main__":
    filename = sys.argv[1]
    os.system(
        f'tshark -r {filename} -T fields -Y "http.request.method == POST" -e http.file_data > request_data.txt'
    )
    os.system(
        f'tshark -r {filename} -T fields -Y "http.response.code==200" -e http.file_data > response_data.txt'
    )
    if is_Godzilla():
        godzilla = godzilla.Godzilla()
        godzilla.decode_All()
