'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: WeWorkAddress.py
@time: 2021/3/28 19:31
@Email: Warron.Wang
'''

import json

import requests

class WeWorkAddress:
    def __init__(self):
        self.token = self.get_token()

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
        r = requests.get(url= url, params= params)
        # print(type(r.json()), r.json())  # dict
        return r.json()["access_token"]

    # 获取通讯录某个成员
    def get_information(self, user_id: str):
        '''
        获取用户信息
        :param user_id:
        :return:
        '''
        # user_id = "CeShi17"
        proxies = {
            "https": "http://127.0.0.1:8888",
            "http": "http://127.0.0.1:8888"
        }
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get"
        params = {"access_token": self.token,
                  "userid": user_id
        }
        # r = requests.get(url= url, proxies= proxies, verify=False)
        r = requests.get(url= url, params= params)
        json1 = json.dumps(json.loads(r.text), indent=4, sort_keys=False, ensure_ascii=False)
        # 打印字典对象
        # print(r.json())

        # 打印json格式
        # print(json1)
        # assert "测试05" == r.json()["name"]
        return r.json()


    # 添加通讯录成员
    def create_member(self, userid: str, name: str, mobile: str, department: list):
        '''
        创建成员
        :param name: CeShi17
        :param mobile: 手机号11位
        :param department: 部门
        :return:
        '''
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department,
            "position": "产品主管",
            "gender": "1",
            "email": "zhangsans@gzdev.com"
        }
        # r = requests.post(url= url, data= json.dumps(data))
        # 或
        r = requests.post(url= url, json= data)
        # print(r.json())
        return r.json()

    # 更新通讯录成员
    def update_member(self, userid: str, name: str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": userid,
            "name": name,
            "mobile": "+86 13900000008",
        }
        r = requests.post(url= url, json= data)
        # print(r.json())
        return r.json()

    # 删除通讯录成员
    def delete_member(self, user_id):
        # self.userid = "CeShi17"
        params = {"access_token": self.token,
                  "userid": user_id
        }
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        r = requests.get(url= url, params= params)
        # print(r.json())
        return r.json()