'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_webdriverwait.py
@time: 2021/2/20 09:57
@Email: wei1.wang@ximalaya.com
'''

import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

class TestWebdriverWait():
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
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        '''
        元素定位高阶用法
        :return:
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/stockName" and @text="阿里巴巴"]').click()
        self.driver.find_element_by_xpath('//*[@text="BABA"]').click()
        #切换到 股票tab
        self.driver.find_element_by_xpath('//*[contains(@resource-id,"title_container")]//*[@text="股票"]').click()
        #获取股票价格，加个显示等待
        locator = (MobileBy.XPATH,'//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]')
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # ele = self.driver.find_element(*locator)
        ele = WebDriverWait(self.driver, 10).until(lambda x:x.find_element(*locator))
        print(f"当前09988股票对应的股票价格是：{ele.text}")
        current_price = float(ele.text)
        expect_price = 240
        assert current_price > expect_price
        assert_that(current_price, close_to(expect_price, expect_price*0.1))
