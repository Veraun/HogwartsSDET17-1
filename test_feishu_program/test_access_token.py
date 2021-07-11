'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_access_token.py
@time: 2021/7/7 16:26
@Email: Warron.Wang
'''
import json

import requests

def test_token():
    BASE_URL = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
    HEADER = {
        "Content-Type": "application/json;charset=utf-8"
    }
    PARAMS = {
    "app_id":"cli_a06fdb373efb100b",
    "app_secret":"YMw4bRJOfxeOsh58rShffQhIJQaeSVqr"
    }

    r = requests.post(url=BASE_URL, headers=HEADER, data=json.dumps(PARAMS))
    res = r.json()
    # print(res["tenant_access_token"])
    # print(r.json())
    return res

def get_users():
    token = test_token()["tenant_access_token"]
    print(token)
    BASE_URL = "https://open.feishu.cn/open-apis/contact/v3/users"
    HEADER = {
        "Authorization": str(token)
    }
    r = requests.get(url=BASE_URL, headers = HEADER)
    print(r.text)


if __name__ == '__main__':
    print(get_users())