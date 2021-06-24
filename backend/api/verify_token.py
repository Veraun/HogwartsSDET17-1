'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: business-test-pytest
@file: verify_token.py
@time: 2021/6/7 11:42
@Email: Warron.Wang
'''
from flask import g
from flask_httpauth import HTTPBasicAuth


# 初始化 auth
from backend.data_base.user_table import User

auth = HTTPBasicAuth()


'''
auth 的 username在登录时是用户名，但是在登录后是token
'''
# 编写回调函数，当进行登录时，会回调此函数
@auth.verify_password
def verify_password(username, password):
    print(username)
    print(password)
    # 进行token校验
    user = User.check_token(username)
    # 如果校验结果是错误，或者超时，就认为是登录接口操作
    if not user:
        # 从数据库中查询用户信息
        user = User.query.filter_by(username= username).first()
        # 如果用户不存在，或者密码不匹配，就会校验失败
        if not user or user.password != password:
            return False

    # 如果校验结果是token符合要求 或 用户名密码正确，就认为此时是其他接口(如：获取用例)
    # flask的g代表flask的本地线程变量 -> flask线程可共享使用
    g.user = user
    return True
