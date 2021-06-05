#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 16:47
# @Author  : Warren.wang
# @File    : test_fixture_5_1.py
# @Software: PyCharm
import pytest
import datetime
'''
@pytest.fixture()  #默认是False
@pytest.fixture(autouse=True)  #自动执行
'''

# @pytest.fixture()  # 默认是False
@pytest.fixture(autouse=True)  # 自动执行
def login():
    print("登录操作")
    token = datetime.datetime.now()
    yield token  # yield 相当于return
    print("登出操作")
    # return token

@pytest.fixture()
def get_username(login):
    print(login)
    name = "赫敏"
    print(name)
    return name


def test_search(get_username):
    print("搜索")


def test_cart(login):
    print(login)
    print("购物")


def test_order():
    print(login)
    print("下单")