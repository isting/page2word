#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import random
import hashlib
import json

appid = '20190813000326115'
secretKey = 'OaD28VBAOxn7_fVntnQF'


def translate(k, i, dataLen):
    q = k
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode())
    sign = m1.hexdigest()

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
    }
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    data = {
        'q': q,
        'from': 'en',
        'to': 'zh',
        'appid': appid,
        'salt': salt,
        'sign': sign
    }
    result = requests.post(url=url, headers=headers, data=data, timeout=10)
    content = json.loads(result.content)

    print("{}/{}".format(i, dataLen), "单词：{}，翻译：{} \n".format(k, content['trans_result'][0]['dst']))
    return "单词：{}，翻译：{} \n".format(k, content['trans_result'][0]['dst'])
    # save("单词：{}，翻译：{} \n".format(k, content['trans_result'][0]['dst']))

def save(data):
  with open('data/translate_data.txt', 'a', encoding="utf-8") as f:
    f.write(data)

