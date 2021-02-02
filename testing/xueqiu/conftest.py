#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 9:16
# @Author  : Warren.wang
# @File    : conftest.py
# @Software: PyCharm
import datetime
import pytest


@pytest.fixture(scope="session")
def login():
    print("登录操作>>>>")
    name = "哈利波特"
    yield name  #yield相当于return
    print("登出操作>>>")
