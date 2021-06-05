#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 9:52
# @Author  : Warren.wang
# @File    : test_calc_1.py
# @Software: PyCharm

# 计算器 相加功能
def add(a, b):
    return a + b


# python包：创建包时会自动创建__init__.py；可以被其他文件导入
#python目录：没有__init__.py；不可以被其他文件导入



# 测试用例命名规范
# 文件要在test_开头，或者_test结尾
# 类要以Test开头，方法要以test_开头
def test_add():
    assert 2 == add(1, 1)
