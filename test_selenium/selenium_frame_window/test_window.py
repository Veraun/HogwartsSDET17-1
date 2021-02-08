#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 9:29
# @Author  : Warren.wang
# @File    : test_window.py
# @Software: PyCharm

'''
多窗口切换
通过句柄(窗口的唯一识别id)
'''
from time import sleep

from selenium import webdriver

from test_selenium.selenium_frame_window.base import Base


class TestWindow(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        #打印当前窗口
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        #打印当前窗口
        print(self.driver.current_window_handle)
        #打印所有窗口:是个list
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        #切换到新窗口
        self.driver.switch_to_window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("password")
        sleep(2)
        #切换回上一个窗口
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("login_username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("login_password")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)