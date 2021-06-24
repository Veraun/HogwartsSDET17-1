'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: business-test-pytest
@file: login.py
@time: 2021/6/7 11:28
@Email: Warron.Wang
'''
from flask import g
from flask_restful import Resource

from backend.api.verify_token import auth


class Login(Resource):
    # method_decorators 代表给Login 接口添加一个装饰器。下面的get表示对get接口进行添加
    # auth.login_required 是httpAuth的用法，添加了此装饰器的对象会回调校验token方法
    method_decorators = {'get': [auth.login_required]}

    def get(self):
        # 使用 verify_password中，校验成功后的用户信息
        token = g.user.generate_token()
        return {"access_token": token}

