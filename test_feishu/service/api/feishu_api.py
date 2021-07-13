'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: feishu_api.py
@time: 2021/7/11 17:06
@Email: Warron.Wang
'''


class FeishuApi:
    '''
    飞书的api公共特性，获取token，获取身份信息、断言状态码为200 或者code为0 或msg
    '''

    def __init__(self):
        self.token: str = None

    def get_token(self):
        pass

    def check_success(self):
        pass
