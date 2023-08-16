# @Author: s1rius
# @Date: 2023-08-15 11:13:02
# @LastEditTime: 2023-08-15 15:39:35
# @Description: https://s1rius.space/

import base64
import gzip
from hashlib import md5
import os
import sys
from urllib.parse import unquote


def main():
    godzilla = Godzilla()
    godzilla.decode_All()
    # godzilla.response_decode()


class antSwords(object):
    def __init__(self):
        self.key = 0


class Godzilla(object):
    def __init__(self):
        self.key = "421eb7f1b8e4b3cf"
        self.passwd = "babyshell"

    def decode_All(self):
        f = open("data.txt", "w")
        req_command = self.request_decode()
        res_command = self.response_decode()
        if len(req_command) == len(res_command):
            for i in range(len(req_command)):
                f.write(
                    f"{i + 1}:\n{req_command[i]}\n\n{res_command[i]}\n----------------------------\n"
                )
        os.remove("request_data.txt")
        os.remove("response_data.txt")

    def xor_Base64_decode(self, D, K):  # godzila_PHP_Eval_Xor_Base64_decode
        D = bytearray(base64.b64decode(D))
        K = K.encode("utf-8")
        for i in range(len(D)):
            c = K[(i + 1) & 15]
            D[i] ^= c
        try:
            data = gzip.decompress(D).decode("utf8")
        except:
            data = D.decode("latin1")
        finally:
            return data

    def request_decode(self):
        req_list = []
        os.system(
            f'tshark -r {file_name} -T fields -Y "http.request.method == POST" -e http.file_data > request_data.txt'
        )
        with open("request_data.txt") as f:
            lines = f.readlines()
            for line in lines:
                shell = unquote(line.split("&")[1].split("=")[1])
                if len(shell) <= 300:
                    request = self.xor_Base64_decode(shell, self.key)
                    if "cmdLine" in request:
                        req_command = request.split(";")[1].split('"')[0].strip()
                    else:
                        req_command = request[15:]
                    req_list.append(req_command)
        return req_list

    def response_decode(self):
        os.system(
            f'tshark -r {file_name} -T fields -Y "http.response.code==200" -e http.file_data > response_data.txt'
        )

        with open("response_data.txt") as f:
            res_list = []
            lines = f.readlines()
            for line in lines:
                if (
                    md5((self.passwd + self.key).encode("utf-8")).hexdigest()[:16]
                    in line
                ):  # 筛选哥斯拉shell返回值
                    code = line[16:-17]
                    # print(code)
                    response_Code = self.xor_Base64_decode(code, self.key)
                    res_list.append(response_Code)
        return res_list


if __name__ == "__main__":
    file_name = sys.argv[1]
    main()
