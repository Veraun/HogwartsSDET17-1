#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import allure
import pytest
import yaml

sys.path.append('..')
print(sys.path)
from pythoncode.Calculator import Calculator



#使用fixture
@pytest.fixture(scope="session")
def get_instance():
    print("开始计算...")
    calc: Calculator = Calculator()
    yield calc
    print("结束计算...")


# def test_param(get_datas_with_fixture):
#     print(get_datas_with_fixture)


# yaml json excel csv xml
# 测试类
@allure.feature("计算器")
class TestCalc:
    # datas: list = get_datas()
    # add_int_data = get_datas('add', 'int')
    # div_int_data = get_datas('div', 'int_error')

    # @pytest.mark.parametrize("a, b, result", add_int_data[0], ids=add_int_data[1])
    # def test_add(self,get_instance, a, b, result):
    #     assert result == get_instance.add(a, b)

    #第二次改造
    # @allure.title("相加_{get_datas_with_fixture[0]}_{get_datas_with_fixture[1]}")
    # @allure.story("相加功能")
    # def test_add(self, get_instance, get_datas_with_fixture):
    #     f = get_datas_with_fixture
    #     assert f[2] == get_instance.add(f[0], f[1])
    #
    # @pytest.mark.parametrize("a,b,result", [
    #     [0.1, 0.1, 0.2],
    #     [0.1, 0.2, 0.3]
    # ])
    # def test_add_float(self, get_instance, a, b, result):
    #     assert result == round(get_instance.add(a, b), 2)
    #
    # # 除数为0
    # @pytest.mark.parametrize("a, b, result", div_int_data[0], ids=div_int_data[1])
    # def test_div_0(self, get_instance, a, b, result):
    #     with pytest.raises(ZeroDivisionError):
    #         result = get_instance.div(a, b)

    #第三次改造
    @allure.title("add_{get_add_int_datas_with_fixture[0]}_{get_add_int_datas_with_fixture[1]}")
    @allure.story("Add Integer Function")
    def test_add_int(self, get_instance, get_add_int_datas_with_fixture):
        f = get_add_int_datas_with_fixture
        assert f[2] == get_instance.add(f[0], f[1])

    @allure.title("add_{get_add_float_datas_with_fixture[0]}_{get_add_float_datas_with_fixture[1]}")
    @allure.story("Add float Function")
    def test_add_float(self, get_instance, get_add_float_datas_with_fixture):
        f = get_add_float_datas_with_fixture
        assert f[2] == round(get_instance.add(f[0], f[1]), 8)

    @allure.title("div_{get_div_int_normal_datas_with_fixture[0]}_{get_div_int_normal_datas_with_fixture[1]}")
    @allure.story("div Integer normal Function")
    def test_div_int_normal(self, get_instance, get_div_int_normal_datas_with_fixture):
        f = get_div_int_normal_datas_with_fixture
        print("f",f)
        assert f[2] == get_instance.div(f[0], f[1])

    @allure.title("div_{get_div_int_error_datas_with_fixture[0]}_{get_div_int_error_datas_with_fixture[1]}")
    @allure.story("div Integer error Function")
    def test_div_int_zero(self, get_instance, get_div_int_error_datas_with_fixture):
        f = get_div_int_error_datas_with_fixture
        with pytest.raises(ZeroDivisionError):  # pytest inner function
            get_instance.div(f[0], f[1])


if __name__ == '__main__':
    pytest.main(["-vs", "test_calculatorNew.py"])