'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: demoPage.py
@time: 2021/7/13 17:58
@Email: Warron.Wang
'''

# coding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from test_feishu.app.page import dashPage
import time


class demoWebPage(dashPage.WebPage):
    '''
    demoWebPage继承dashPage.WebPage，而dashPage.WebPage继承了dashPage.AutomationPage
    利用了python的层级继承关系
    '''
    username_loc = (By.ID, 'l-1')
    password_loc = (By.ID, 'l-2')
    loginButton_loc = (By.ID, 'l-4')

    def inputUserName(self, username):
        self.findElement(*self.username_loc).send_keys(username)
        time.sleep(2)

    def inputPasswd(self, password):
        self.findElement(*self.password_loc).send_keys(password)
        time.sleep(2)

    def clickLogin(self):
        self.findElement(*self.loginButton_loc).click()
        time.sleep(2)

    def login(self, username='admin', password='admin'):
        self.goTo('http://my.weke.com/login.html')
        self.inputUserName(username)
        self.inputPasswd(password)
        self.clickLogin()
