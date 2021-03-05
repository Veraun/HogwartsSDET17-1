'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_baidu_window.py
@time: 2021/2/24 14:54
@Email: Warron.wang
'''
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Testsearch:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(10)
    def teardown(self):
        # self.driver.quit()
        pass
    def test_search(self):

        self.driver.find_element(By.ID,'kw').send_keys('python')
        self.driver.find_element_by_id('su').click()
        self.driver.find_element(By.LINK_TEXT,'Python(计算机编程语言) - 百度百科').click()

        handle = self.driver.window_handles
        # print(handle)
        self.driver.switch_to_window(handle[-1])
        self.driver.find_element(By.XPATH, '//*[@title="英文单词"]').click()