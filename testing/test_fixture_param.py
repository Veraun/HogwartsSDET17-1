#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 11:18
# @Author  : Warren.wang
# @File    : test_fixture_param.py
# @Software: PyCharm
import pytest

#使用fixture实现参数化
@pytest.fixture(params=['hali','赫敏'])
def login(request):
    print("login")
    return request.param

def test_search(login):
    print(login)
    print("搜索")