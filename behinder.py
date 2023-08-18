# @Author: s1rius
# @Date: 2023-08-18 16:55:18
# @LastEditTime: 2023-08-18 17:59:17
# @Description: https://s1rius.space/

import base64
from Crypto.Cipher import AES

import main


class Behinder(object):
    def __init__(self):
        self.key = ""
        self.passwd = ""

    def XOR(K, D):
        result = []
        for i in range(len(D)):
            c = K[i + 1 & 15]
            if not isinstance(D[i], int):
                d = ord(D[i])
            else:
                d = D[i]
            result.append(d ^ ord(c))
        return b"".join([i.to_bytes(1, byteorder="big") for i in result])

    def regexphp(regexphp, destr):
        match = re.findall(regexphp, str(destr))
        try:
            restr = base64.b64decode(match[0].encode("utf-8"))
        except Exception as e:
            print(e)
            restr = base64.b64decode(match[0].encode("gb2312"))
        return restr

    def decrypt_req_payload(self, payload):
        encrypted_text = base64.b64decode(payload)
        try:
            cipher = AES.new(key=self.key.encode(), mode=AES.MODE_CBC, iv=b"\x00" * 16)
            decrypted_text = cipher.decrypt(encrypted_text)
        except Exception as e:
            decrypted_text = self.XOR(self.key, base64.b64decode(payload))
        decrypted_text = self.regexphp(r"64_decode\('(.*)'\)", decrypted_text)
        return decrypted_text

    def decrypt_res_payload(self, payload):
        encrypted_text = base64.b64decode(payload)
        try:
            cipher = AES.new(key=self.key.encode(), mode=AES.MODE_CBC, iv=b"\x00" * 16)
            decrypted_text = cipher.decrypt(encrypted_text)
        except Exception as e:
            decrypted_text = self.XOR(self.key, base64.b64decode(payload))
        # decrypted_text = regexphp(r"64_decode\('(.*)'\)", decrypted_text)
        # msg = regexphp(r"\"msg\":\"(.*)\"}", decrypted_text)
        # status = regexphp(r"\"status\":\"(.*)\"", decrypted_text)
        # decrypted_text = '''"status":"{}","msg":"{}"'''.format(status.decode(),msg.decode())
        return decrypted_text
