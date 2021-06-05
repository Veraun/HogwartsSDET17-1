'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_calculator_2.py
@time: 2021/5/29 10:17
@Email: Warron.Wang
'''
import sys

import pytest

sys.path.append("..")
print("root_path", sys.path)

from pythoncode.Calculator import Calculator


class TestCalc:

    # 前置条件：类级别
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()  # 实例变量

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.search  #加标签
    def test_add(self):
        # calc = Calculator()
        assert 3 == self.calc.add(1, 2)

    @pytest.mark.login  #加标签
    def test_div(self):
        pass
