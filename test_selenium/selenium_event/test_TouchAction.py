#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 17:50
# @Author  : Warren.wang
# @File    : test_TouchAction.py
# @Software: PyCharm
from time import sleep
'''
TouchActions
模拟PC端和移动端的点击，滑动，拖拽，多点触控等多种手势操作
'''

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c",False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        '''
        滑动到底部，点击下一页
        点击下一页
        :return:
        '''
        self.driver.get("https://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        el_search = self.driver.find_element_by_id("su")
        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()

        action.scroll_from_element(el,0,10000).perform()
