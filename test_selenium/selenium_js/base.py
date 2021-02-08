#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 9:33
# @Author  : Warren.wang
# @File    : base.py
# @Software: PyCharm

'''
在待执行的py文件下，执行如下命令
mac电脑：browser=chrome pytest test_frame.py
windows：先set browser=chrome 后pytest test_frame.py
'''
import importlib
from selenium import webdriver
import os

class Base:
    def setup(self):
        browser = os.getenv("browser")
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "headless":
            self.driver = webdriver.phantomjs()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Chrome()

        if self.driver == None:
            exit()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
