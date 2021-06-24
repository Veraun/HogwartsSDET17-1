'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: business-test-pytest
@file: test_login.py
@time: 2021/6/7 15:43
@Email: Warron.Wang
'''

import requests

class TestLogin:
    BASE_URL = "http://localhost:5000"
    def test_login(self):
        # 其中 auth 标识要输入的校验信息，比如 账号和密码
        r = requests.get(self.BASE_URL + '/login', auth=("warron",123456))
        assert "access_token" in r.json()

        r = requests.get(self.BASE_URL + '/login', auth=("warron", 12345678))
        assert r.status_code == 401
