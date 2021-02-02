#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 17:07
# @Author  : Warren.wang
# @File    : conftest.py
# @Software: PyCharm

'''
要点1：文件名时固定的，不能改
要点2：执行测试用例之前，先去执行conftest文件
'''

import datetime
from typing import List
import pytest


@pytest.fixture(scope="session")
def login():
    print("登录操作>>>>")
    token = datetime.datetime.now()
    yield token  #yield相当于return
    print("登出操作>>>")
    # return token



def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    pass