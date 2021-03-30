#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 20:03
# @Author  : Warren.wang
# @File    : test_demo.py
# @Software: PyCharm
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.android.settings.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.quit()