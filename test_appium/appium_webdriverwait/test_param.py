'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_param.py
@time: 2021/2/22 12:52
@Email: wei1.wang@ximalaya.com
'''

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

class TestParam():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'  # 去掉页面弹窗
        # desired_caps['dontStopAppOnReset'] = 'true'  # 启动时不停止app(提升app运行速度)
        desired_caps['skipServerInstallation'] = 'true'  # 跳过安装、权限设置等操作(提升app运行速度)
        desired_caps['unicodeKeyBoard'] = 'true'  # case里输入如果有中文，需要设置
        desired_caps['resetKeyBoard'] = 'true'  # case里输入如果有中文，需要设置
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_search(self):
        pass