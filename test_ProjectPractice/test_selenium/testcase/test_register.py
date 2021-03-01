'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_register.py
@time: 2021/3/1 16:53
@Email: wei1.wang@ximalaya.com
'''
from time import sleep

from test_ProjectPractice.test_selenium.home_page.main_page import MainPage


class TestRegister:
    def test_register(self):
        '''
        从首页-注册页
        :return:
        '''
        main = MainPage()
        main.goto_register().register()
        sleep(3)

    def test_login_register(self):
        '''
        从首页-登录页-注册页
        :return:
        '''
        main = MainPage()
        main.goto_login().goto_register().register()
        sleep(3)
