#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 11:18
# @Author  : Warren.wang
# @File    : test_fixture_param_7.py
# @Software: PyCharm
import pytest

#使用fixture实现参数化
@pytest.fixture(params=['hali','赫敏'], ids=['aa', 'bb'])
def login(request):   # request也是一个fixtrue
    print("login")
    return request.param  # request.param 拿到参数

def test_search(login):
    print(login)
    print("搜索")