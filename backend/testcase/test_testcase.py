'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: business-test-pytest
@file: test_testcase.py
@time: 2021/6/7 17:05
@Email: Warron.Wang
'''
import requests


class TestTestCase:
    def test_right_testcase(self):
        r = requests.get("http://localhost:5000/login", auth=("warron",123456))
        token = r.json().get("access_token")
        r= requests.get("http://localhost:5000/testcase/get", auth=(token, ""))
        print(r.json())
        assert r.status_code == 200
        assert r.json().get("msg") == "OK"


    def test_error_testcase(self):
        token =''
        r= requests.get("http://localhost:5000/testcase/get", auth=(token, ""))
        assert r.status_code == 401
