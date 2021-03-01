'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_address.py
@time: 2021/3/1 17:17
@Email: wei1.wang@ximalaya.com
'''
from test_ProjectPractice.test_selenium.address_page.main_page import MainPage


class TestAddress:
    def test_add_member(self):
        main = MainPage()
        main.goto_address().add_member()