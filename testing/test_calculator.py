#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 9:58
# @Author  : Warren.wang
# @File    : test_calculator.py
# @Software: PyCharm
import sys

import pytest
import yaml

sys.path.append('..')
print("rootpath", sys.path)

from pythoncode.Calculator import Calculator

# yaml json excel csv xml
#解析测试数据
def get_datas(type):
    with open("./datas/calc.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        # print(datas)
    return (datas[type]["datas"], datas[type]['ids'])

#测试类
class TestCalc:
    datas_add:list = get_datas('add')
    datas_div:list = get_datas('div')
    datas_mul:list = get_datas('multiply')
    datas_sub:list = get_datas('subtract')

    #前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    #后置条件
    def teardown_class(self):
        print("结束计算")

    # @pytest.mark.login  #加标签
    # @pytest.mark.parametrize("a, b, result",[
    #     [1,1,2],[100,400,300],[1,0,1]
    # ])
    @pytest.mark.parametrize("a, b, expect", datas_add[0], ids= datas_add[1])
    def test_add(self, a, b, expect):
        print(f"a={a}, b={b}, result={expect}")
        assert expect == self.calc.add(a, b)

    #浮点数：特殊处理
    @pytest.mark.parametrize("a, b, expect", [
        [0.11,0.12,0.23],[0.1,0.2,0.3]
    ])
    def test_add_float(self, a, b, expect):
        print(f"a={a}, b={b}, result={expect}")
        assert expect == round(self.calc.add(a, b), 2)

    #使用for循环，当里面出现fail就会break掉，不推荐
    # def test_add1(self):
    #     datas = [[1,1,2],[100,400,300],[1,0,1]]
    #     for data in datas:
    #         print(data)
    #         assert data[2] == self.calc.add(data[0], data[1])

    @pytest.mark.parametrize("a, b, expect", datas_div[0], ids= datas_div[1])
    def test_div(self, a, b, expect):
        # with pytest.raises(ZeroDivisionError):
        print(f"a={a}, b={b}, result={expect}")
        assert expect == self.calc.div(a, b)

    #除不尽
    @pytest.mark.parametrize("a, b, expect", [
        [10,3,3.33],[10,-3,-3.33],[-10,-3,3.33]
    ])
    def test_div_indivisible(self, a, b, expect):
        print(f"a={a}, b={b}, result={expect}")
        assert expect == round(self.calc.div(a, b), 2)

    #被除数是0
    @pytest.mark.parametrize("a, b", [
        [0.1, 0], [10, 0], [-10, 0]
    ])
    def test_div_zero(self, a, b):
        print(f"a={a}, b={b}")
        with pytest.raises(ZeroDivisionError): #抛出这个异常ZeroDivisionError
            self.calc.div(a, b)

    @pytest.mark.parametrize("a, b, expect", datas_mul[0], ids=datas_mul[1])
    def test_mul(self, a, b, expect):
        print(f"a={a}, b={b}, result={expect}")
        assert expect == self.calc.mul(a, b)

    @pytest.mark.parametrize("a, b, expect", [
        [0.11, 0.12, 0.01], [0.1, 0.2, 0.02]
    ])
    def test_mul_float(self, a, b, expect):
        print(f"a={a}, b={b}, result={expect}")
        assert expect == round(self.calc.mul(a, b), 2)


    @pytest.mark.parametrize("a, b, expect", datas_sub[0], ids=datas_sub[1])
    def test_sub(self, a, b, expect):
        print(f"a={a}, b={b}, result={expect}")
        assert expect == self.calc.sub(a, b)

    @pytest.mark.parametrize("a, b, expect", [
        [0.11, 0.12, -0.01], [0.1, 0.2, -0.1]
    ])
    def test_sub_float(self, a, b, expect):
        print(f"a={a}, b={b}, result={expect}")
        assert expect == round(self.calc.sub(a, b), 2)

if __name__ == '__main__':
    pytest.main(["-v","-s"])