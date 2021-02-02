#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 17:44
# @Author  : Warren.wang
# @File    : test_yield.py
# @Software: PyCharm
import pytest
import datetime
'''
作用域（session>module>class>function）
-function函数或方法级别都会被调用
-class类级别调用一次
-module模块级别调用一次
-session时多个文件调用一次(可以跨.py文件调用，每个.Py文件就是module)
'''

@pytest.fixture(scope='module')  #作用域于整个模块，只运行一次
def login():
    print("登录操作")
    token = datetime.datetime.now()
    yield token  #yield相当于return
    print("登出操作")
    # return token


def test_search():
    print("搜索")

def test_cart(login): #能获取fixture:login的返回值
    print(login)
    print("购物")

@pytest.mark.usefixtures("login") #获取fixture:login的返回值时拿不到的
def test_order():
    print(login)
    print("下单")