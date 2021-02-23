'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_browser.py
@time: 2021/2/23 11:26
@Email: wei1.wang@ximalaya.com
'''

from appium import webdriver
from time import sleep

class TestBrowser():
    def setup(self):
        des_caps = {
            "platformName": "android",
            "platformVersion": "6.0.1",
            "browserName": "Browser",  # 被测浏览器
            "deviceName": "emulator-5554",
            "noReset": True,  # 去掉页面弹窗
            "chromedriverExecutable": "/Users/xmly/Documents/chromedriver20"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        sleep(5)