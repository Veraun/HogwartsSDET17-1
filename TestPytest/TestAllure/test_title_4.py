'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_title_4.py
@time: 2021/5/28 10:52
@Email: Warron.Wang
'''

'''
报告：测试用例名字显示中文
'''
import allure


@allure.title("登录成功")
def test_a():
    print("登录成功")