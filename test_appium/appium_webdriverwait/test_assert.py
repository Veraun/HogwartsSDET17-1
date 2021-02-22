'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_assert.py
@time: 2021/2/22 12:24
@Email: wei1.wang@ximalaya.com
'''

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

class TestGetAssert():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'  # 去掉页面弹窗
        # desired_caps['dontStopAppOnReset'] = 'true'  # 启动时不停止app(提升app运行速度)
        desired_caps['skipDeviceInitialization'] = 'true'  # 跳过安装、权限设置等操作(提升app运行速度)
        desired_caps['unicodeKeyBoard'] = 'true'  # case里输入如果有中文，需要设置
        desired_caps['resetKeyBoard'] = 'true'  # case里输入如果有中文，需要设置
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    @pytest.mark.skip
    def test_assert1(self):
        search_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(search_ele.get_attribute("content-desc"))
        print(search_ele.get_attribute("resource-id"))
        print(search_ele.get_attribute("enabled"))
        print(search_ele.get_attribute("clickable"))
        print(search_ele.get_attribute("bounds"))
        assert 'search' in search_ele.get_attribute("resource-id")

    @pytest.mark.skip
    def test_assert2(self):
        a = 10
        b = 20
        assert a < b
        assert 'h' in 'this'

    def test_hamcrest(self):
        assert_that(10, equal_to(9), "这是一个测试")
        assert_that(8, close_to(10,2)) #断言：数字接近
        assert_that("contains some string", contains_string("string"))
