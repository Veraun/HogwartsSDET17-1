#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 12:25
# @Author  : Warren.wang
# @File    : test_js.py
# @Software: PyCharm
import time

import pytest
from selenium.webdriver.common.by import By

from test_selenium.selenium_js.base import Base


class TestJs(Base):
    @pytest.mark.skip
    #上下滑动页面
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        #执行js代码块，有返回值
        element = self.driver.execute_script('return document.getElementById("su")')
        element.click()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        time.sleep(2)

        # print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))
        for code in [
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    #获取日期控件
    @pytest.mark.skip
    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        date_js = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        time.sleep(1)
        self.driver.execute_script("document.getElementById('train_date').value='2021-06-20'")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))

    # @pytest.mark.skip
    def test_hotel(self):
        self.driver.get("https://hotels.ctrip.com/")
        self.driver.maximize_window()
        # time.sleep(3)
        # self.driver.find_element(By.ID, "hotels-destination").click()
        # time.sleep(3)
        # js = 'document.getElementById("hotels-destination").value ="武汉"'
        # self.driver.execute_script(js)
        # time.sleep(3)
        # print(self.driver.execute_script("return document.getElementById('hotels-destination').value"))
        # self.driver.find_element(By.XPATH, '//*[@class="search-btn-wrap"]').click() # '//*[@class="search-btn-wrap"]'
        time.sleep(5)
        self.driver.find_element(By.ID, "hotels-destination").clear()
        self.driver.find_element(By.ID, "hotels-destination").send_keys("常德")
        time.sleep(3)
        # js = 'document.getElementById("hotels-destination").value ="武汉"'
        # self.driver.execute_script(js)
        # time.sleep(3)
        # print(self.driver.execute_script("return document.getElementById('hotels-destination').value"))
        self.driver.find_element(By.XPATH, '//*[@class="search-btn-wrap"]').click() # '//*[@class="search-btn-wrap"]'
