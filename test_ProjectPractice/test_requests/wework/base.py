'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: base.py
@time: 2021/3/29 10:54
@Email: Warron.Wang
'''
import requests


class Base:
    def __init__(self):
        # session:1减少ssl连接的开销
        self.s = requests.session()
        self.token = self.get_token()
        # session:2维持会话
        self.s.params = {"access_token": self.token}

    # 获取token
    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {"corpid": "ww0644cdc8a2b875a9",
                  "corpsecret": "fyOJ04lJyhJvyAkypqfZlBC7w34mtL7wpEJ1UQnRFUw"}

        # 设置代理，charles就可以抓到请求了.charlse代理：127.0.0.1:8888
        proxies = {
            "https": "http://127.0.0.1:8888",
            "http" : "http://127.0.0.1:8888"
        }
        # r = requests.get(url= url, proxies= proxies, verify=False) # verify=False，关闭就不会进行ssl证书校验
        r = self.s.get(url= url, params= params)
        # print(type(r.json()), r.json())  # dict
        return r.json()["access_token"]

    def send(self, *args, **kwargs):
        return self.s.request(*args, **kwargs)
