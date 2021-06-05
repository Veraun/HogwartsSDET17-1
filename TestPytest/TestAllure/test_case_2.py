'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_case_2.py
@time: 2021/5/27 19:49
@Email: Warron.Wang
'''

import allure

TEST_CASE_LINK = "https://github.com/issure?id=111"
@allure.testcase(TEST_CASE_LINK, "test case title")
def test_with_testcase():
    pass