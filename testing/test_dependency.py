#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/2 19:53
# @Author  : Warren.wang
# @File    : test_dependency.py
# @Software: PyCharm

'''
B依赖A，如果A执行失败，那么B不会执行
'''
import pytest

@pytest.mark.dependency()
@pytest.mark.xfail(reason="deliberate fail")
def test_a(): #失败的case
    assert False

@pytest.mark.dependency()
def test_b():
    pass

@pytest.mark.dependency(depends=["test_a"])
def test_c(): #不执行，跳过
    pass

@pytest.mark.dependency(depends=["test_b"])
def test_d():
    pass

@pytest.mark.dependency(depends=["test_b","test_c"])
def test_e(): #不执行，跳过
    pass