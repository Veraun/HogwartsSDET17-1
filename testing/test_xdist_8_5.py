#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 20:02
# @Author  : Warren.wang
# @File    : test_xdist_8_5.py
# @Software: PyCharm
'''
多线程并行与分布式执行
用例多的时候效果明显
pytest xx.py -n numbers(根据电脑实际情况，不是越大越好)
pytest xx.py -n auto  (auto自动分配)
'''

import pytest

def test_a():
    assert False

def test_b():
    pass

def test_c():
    pass

def test_d():
    pass

def test_e():
    pass