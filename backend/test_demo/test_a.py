'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: business-test-pytest
@file: test_a.py
@time: 2021/6/18 14:20
@Email: Warron.Wang
'''


def test_a1():
    print("hello a1")


# nodeid 是用例名字，可以唯一识别一个用例
# 比如 test_02的nodeid就是test_a.py::test_a2
def test_a2():
    print("hello a2")