'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: feishu_api.py
@time: 2021/7/11 17:06
@Email: Warron.Wang
'''
from test_feishu.service.api.base_api import BaseApi


class FeishuApi(BaseApi):
    '''
    飞书的api公共特性，获取token，获取身份信息、断言状态码为200 或者code为0 或msg
    '''

    def __init__(self):
        super().__init__()
        self.token: str = self.get_token()
        self.req.headers = {"Content-Type": "application/json; charset=utf-8"}
        self.req.headers["Authorization"] = f"Bearer {self.token}"

    def get_token(self):
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/"
        json = {
            "app_id": "cli_a06fdb373efb100b",
            "app_secret": "YMw4bRJOfxeOsh58rShffQhIJQaeSVqr"
        }
        res = self.req.post(url, json=json)
        code = res.json()["code"]
        expire = res.json()["expire"]
        if expire == 0:
            raise ConnectionError("秘钥过期了，请更新")
        elif code != 0:
            raise ConnectionError(f"current_code: {code}, expire_code: 0")
        # print(res.json())
        return res.json()["tenant_access_token"]

    def check_success(self, res, type='code', expire=0):
        assert res[type] == expire

    def check_error(self, res, type='code', expire=0):
        assert res[type] != expire
