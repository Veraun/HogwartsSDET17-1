'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: base_api.py
@time: 2021/7/11 17:06
@Email: Warron.Wang
'''
import requests

'''
通用业务封装：
get、post、token
'''


class BaseApi:
    '''
    封装requests等库的细节，实现与具体的请求工具无关，以及做一些简化，或者功能增强
    '''

    def __init__(self):
        self.req = requests.Session()

    def send_request(self, *args, **kwargs):
        return self.req.request(*args, **kwargs)

    def json(self):
        pass
