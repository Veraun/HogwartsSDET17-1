#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 9:49
# @Author  : Warren.wang
# @File    : test_xpathcss.py
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
        '''
        以下四种都是同一个意思
        '''
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        # self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR, "[id=kw]").send_keys("霍格沃兹测试学院")

        self.driver.find_element(By.ID, "su").click()
        self.driver.find_element(By.LINK_TEXT, value="霍格沃兹测试学院 - 主页")

