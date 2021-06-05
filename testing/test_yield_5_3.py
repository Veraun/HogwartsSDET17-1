#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/1 17:44
# @Author  : Warren.wang
# @File    : test_yield_5_3.py
# @Software: PyCharm
import pytest
import datetime
'''
第一种：使用pytest.fixture
第二种：使用pytest.mark.usefixtures("login");注意：如果获取fixture的返回值时拿不到的
'''

# @pytest.fixture(scope='module')  #默认是False
# # @pytest.fixture(autouse=True)  #自动执行
# def login():
#     print("登录操作")
#     token = datetime.datetime.now()
#     yield token  #yield相当于return
#     print("登出操作")
#     # return token


def test_search():
    print("搜索")

def test_cart(login): #能获取fixture:login的返回值
    print(login)
    print("购物")

@pytest.mark.usefixtures("login") #获取fixture:login的返回值时拿不到的
def test_order():
    # print(login)
    print("下单")