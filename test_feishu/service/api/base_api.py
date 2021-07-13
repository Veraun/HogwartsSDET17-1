'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: base_api.py
@time: 2021/7/11 17:06
@Email: Warron.Wang
'''

'''
通用业务封装：
get、post、token
'''


class BaseApi:
    '''
    封装requests等库的细节，实现与具体的请求工具无关，以及做一些简化，或者功能增强
    '''

    def request(self, *args, **kwargs):
        pass

    def json(self):
        pass