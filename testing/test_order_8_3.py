#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 16:27
# @Author  : Warren.wang
# @File    : test_order_8_3.py
# @Software: PyCharm

'''
数字小，先执行
@pytest.mark.run(order=2)
@pytest.mark.third

'''
import pytest


@pytest.mark.run(order=2)
def test_foo():
    assert True


@pytest.mark.run(order=1)
def test_bar():
    assert True


@pytest.mark.third
def test_third():
    assert True