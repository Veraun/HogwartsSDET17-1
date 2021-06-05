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
    @pytest.mark.parametrize("a, b, result", [
        (1,1,2),
        (100,200,300),
        (1,0,1),
    ])
    def test_add(self, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert result == self.calc.add(a, b)

    # 提问：for循环可以实现参数化么？
    # def test_add_1(self):
    #     datas = [
    #     (1,1,2),
    #     (100,200,300),
    #     (1,0,1),
    # ]
    #     for data in datas:
    #         assert data[2] == self.calc.add(data[0], data[1])

    @pytest.mark.login  #加标签
    def test_div(self):
        pass
