# @Author: s1rius
# @Date: 2023-08-15 11:13:02
# @LastEditTime: 2023-08-15 15:39:35
# @Description: https://s1rius.space/

import base64
import gzip
from hashlib import md5
import os
from urllib.parse import unquote

import main


class Godzilla(object):
    def __init__(self):
        self.key = ""
        self.passwd = ""

    def decode_All(self):
        f = open("data.md", "w")  # 覆写操作 注意保存
        req_command = self.request_decode()
        res_command = self.response_decode()
        if len(req_command) == len(res_command):
            for i in range(len(req_command)):
                f.write(f"# {req_command[i]}\n```ini\n{res_command[i]}\n```\n")
        os.remove("request_data.txt")
        os.remove("response_data.txt")
        f.close()
        print("[+] output: ./data.md")

    def xor_Base64_decode(self, D, K):  # godzila_PHP_Eval_Xor_Base64_decode
        D = bytearray(base64.b64decode(D))
        K = K.encode("utf-8")
        for i in range(len(D)):
            D[i] ^= K[(i + 1) & 15]
        try:
            data = gzip.decompress(D).decode("utf-8")
        except:
            data = D.decode("utf-8")
        finally:
            return data

    def request_decode(self):
        req_list = []
        with open("request_data.txt") as f:
            lines = f.readlines()
            if main.is_Godzilla:
                self.passwd = lines[1].split("&")[1].split("=")[0]
                php_encoded = lines[1].split("&")[0].split("=")[1].split("%27")[1]
                php = base64.b64decode("".join(reversed(unquote(php_encoded)))).decode(
                    "utf-8"
                )
                self.key = php.split("key='")[1][:16]
                print(f"[+] key = {self.key}\n[+] pass = {self.passwd}")
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
