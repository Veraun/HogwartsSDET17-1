'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_contact.py
@time: 2021/3/26 14:06
@Email: Warron.Wang
'''
import json

import requests

class TestAddress:
    def setup(self):
        self.token = self.get_token()

    # 获取token
    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww0644cdc8a2b875a9&corpsecret=fyOJ04lJyhJvyAkypqfZlBC7w34mtL7wpEJ1UQnRFUw"

        # 设置代理，charles就可以抓到请求了.charlse代理：127.0.0.1:8888
        proxies = {
            "https": "http://127.0.0.1:8888",
            "http" : "http://127.0.0.1:8888"
        }
        r = requests.get(url= url, proxies= proxies, verify=False) # verify=False，关闭就不会进行ssl证书校验
        # print(type(r.json()), r.json())  # dict
        return r.json()["access_token"]

    # 获取通讯录某个成员
    def test_get_information(self):
        user_id = "CeShi05"
        proxies = {
            "https": "http://127.0.0.1:8888",
            "http": "http://127.0.0.1:8888"
        }
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}"
        r = requests.get(url= url, proxies= proxies, verify=False)
        json1 = json.dumps(json.loads(r.text), indent=4, sort_keys=False, ensure_ascii=False)
        # 打印字典对象
        print(r.json())
        # 打印json格式
        print(json1)
        assert "测试05" == r.json()["name"]

    # 添加通讯录成员
    def test_create_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": "CeShi15",
            "name": "测试15",
            "mobile": "+86 13800000001",
            "department": [1],
            "position": "产品主管",
            "gender": "1",
            "email": "zhangsans@gzdev.com"
        }
        # r = requests.post(url= url, data= json.dumps(data))
        # 或
        r = requests.post(url= url, json= data)
        print(r.json())

    # 更新通讯录成员
    def test_update_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "CeShi15",
            "name": "测试15new",
            "mobile": "+86 13900000001",
        }
        r = requests.post(url= url, json= data)
        print(r.json())

    # 删除通讯录成员
    def test_delete_member(self):
        self.userid = "CeShi15"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={self.userid}"
        r = requests.get(url= url)
        print(r.json())






