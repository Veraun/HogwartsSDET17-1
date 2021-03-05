'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_debug.py
@time: 2021/3/3 09:11
@Email: Warron.wang
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestTmp():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_tmp(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
        self.driver.find_element(By.LINK_TEXT, "霍格沃兹测试学院 – 测试开发工程师的黄埔军校").click()
        self.driver.close()