#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 16:47
# @Author  : Warren.wang
# @File    : test_fixture.py
# @Software: PyCharm
import pytest
import datetime
'''
第一种：使用pytest.fixture
第二种：使用pytest.mark.usefixtures("login")
'''

@pytest.fixture()
def login():
    print("登录")
    yield   #yield相当于return
    print("登出")

@pytest.fixture()
def get_username(login):  #fixture套fixture
    name = "赫敏"
    print(name)
    return name

def test_search():
    print("搜索")

def test_cart(get_username):
    print("购物")

def test_order(login,get_username):
    print("下单")

@pytest.mark.usefixtures("get_username") #远：后执行
@pytest.mark.usefixtures("login")  #近：先执行
def test_order1():
    print(login)
    print("下单1")