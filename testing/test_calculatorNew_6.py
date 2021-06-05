#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

'''
yaml参数化驱动
'''
import sys

import pytest

sys.path.append("..")
print("root_path", sys.path)

from pythoncode.Calculator import Calculator


def get_datas(name, type="int"):
    with open("./datas/test_practice.yml", encoding="utf-8") as f:
        # 将yaml数据流转化为python对象
        all_data = yaml.safe_load(f)
        print(all_data)
    data = all_data[name][type]["datas"]
    ids = all_data[name][type]["ids"]
    return data, ids

@pytest.fixture()
def get_instance():
    print("开始计算")
    calc:Calculator = Calculator()
    yield calc
    print("结束计算")

@pytest.fixture(params=get_datas("add", "int")[0], ids=get_datas("add", "int")[1])
def get_datas_with_fixture(request):
    return request.param


class TestCalc:
    # 类变量：增加类型提示
    add_int_data = get_datas("add", "int")
    add_float_data = get_datas("add", "float")
    div_int_normal_data = get_datas("div", "int_normal")
    div_int_error_data = get_datas("div", "int_error")

    # get_instance实现了，去掉下面

    # 前置条件：类级别
    # def setup_class(self):
    #     print("开始计算")
    #     self.calc = Calculator()  # 实例变量
    #
    # def teardown_class(self):
    #     print("结束计算")

    # @pytest.mark.search  # 加标签
    # @pytest.mark.parametrize("a, b, result", add_int_data[0], ids=add_int_data[1])
    # def test_add(self, get_instance, a, b, result):
    #     print(f"a={a}, b={b}, result={result}")
    #     assert result == get_instance.add(a, b)

    # @pytest.mark.search  # 加标签
    # @pytest.mark.parametrize("a, b, result", add_int_data[0], ids=add_int_data[1])
    def test_add(self, get_instance, get_datas_with_fixture):
        f = get_datas_with_fixture
        assert f[2] == get_instance.add(f[0], f[1])

    @pytest.mark.parametrize("a, b, result", add_float_data[0], ids=add_float_data[1])
    def test_add_float(self, get_instance, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert result == round(get_instance.add(a, b), 3)
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
    @pytest.mark.parametrize("a,b,result", div_int_error_data[0], ids=div_int_error_data[1])
    def test_div_0(self, a, b, result):
        with pytest.raises(ZeroDivisionError):
            result = a / b

    @pytest.mark.parametrize("a,b,result", div_int_normal_data[0], ids=div_int_normal_data[1])
    def test_div_normal(self, get_instance, a, b, result):
        print(f"a={a}, b={b}, result={result}")
        assert result == get_instance.div(a, b)