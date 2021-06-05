'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_feature_1.py
@time: 2021/5/27 18:24
@Email: Warron.Wang
'''

import pytest, allure


@allure.feature("搜索模块")
class TestSearch:
    def test_search_1(self):
        print("case1")

    def test_search_2(self):
        print("case2")


@allure.feature("登录模块")
class TestLogin:
    @allure.story("登录成功")
    @allure.title("登录成功")
    def test_login_success(self):
        with allure.step("步骤1：打开应用"):
            print("打开应用")
        with allure.step("步骤2：进入登录页面"):
            print("进入登录页面")
        with allure.step("步骤3：输入用户名和密码"):
            print("输入用户名和密码")

    @allure.story("登录失败")
    @allure.title("登录失败")
    def test_login_failed_a(self):
        print("这是登录：测试用例，登陆失败")

    @allure.story("用户名缺失")
    @allure.title("用户名缺失")
    def test_login_failed_b(self):
        print("用户名缺失")

    @allure.story("密码缺失")
    @allure.title("密码缺失")
    def test_login_failure(self):
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert "1" == 1
            print("登录失败")

    @allure.story("登录失败")
    @allure.title("登录缺失")
    def test_login_failure_a(self):
        print("这是登录：测试用例，登陆失败")


if __name__ == '__main__':
    pytest.main()
