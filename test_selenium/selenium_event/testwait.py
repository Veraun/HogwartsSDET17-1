#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 12:58
# @Author  : Warren.wang
# @File    : testwait.py
# @Software: PyCharm
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        #2.隐式等待：轮训查找
        self.driver.implicitly_wait(5)
    def test_wait(self):
        # self.driver.find_element(By.XPATH, value='//*[@title="所有分类"]').click()
        self.driver.find_element(By.LINK_TEXT, value="所有分类").click()
        #1.强制等待
        # sleep(3)

        #3.显示等待
        # def wait(x):
        #     #找到这个元素了(至少一个元素)  //*[@id="ember428"]/div[1]
        #     return len(self.driver.find_elements(By.CSS_SELECTOR, value='.table-heading')) >= 1
        # WebDriverWait(self.driver, 12).until(wait)

        #等待时长10秒，默认0.5秒询问一次
        # WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.table-heading')))
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, value='//*[@title = "在最近的一年，一月，一周或一天最活跃的主题"]').click()
        # print("hello")