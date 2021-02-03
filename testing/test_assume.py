#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 19:38
# @Author  : Warren.wang
# @File    : test_assume.py
# @Software: PyCharm

'''
多条断言，互不影响
前面失败，后面会继续执行
'''
import pytest


def test_assume():
    # assert 1 == 1
    # assert 1 == 2
    # assert 2 == 3
    pytest.assume(1 == 1)
    pytest.assume(1 == 2)
    pytest.assume(2 == 3)
    pytest.assume(4 == 4)