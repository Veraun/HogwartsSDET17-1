#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 9:49
# @Author  : Warren.wang
# @File    : test_first.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
        #隱式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.find_element(By.ID, value="kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.ID, value="su").click()
        self.driver.find_element(By.LINK_TEXT, value="霍格沃兹测试学院 - 主页")

