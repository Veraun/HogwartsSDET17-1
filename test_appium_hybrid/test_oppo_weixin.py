'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_webview_apidemo.py
@time: 2021/2/23 17:52
@Email: Warron.wang
'''
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

'''
https://blog.csdn.net/Asaasa1/article/details/109332602
'''
class TestBrowser():
    def setup(self):
        des_caps = {
            "platformName": "android",
            "platformVersion": "10",

            # 企业微信
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.LaunchSplashActivity",

            # 个人微信
            # "appPackage": "com.tencent.mm",
            # "appActivity": "com.tencent.mm.ui.LauncherUI",

            # qq
            # "appPackage": "om.tencent.mobileqq",
            # "appActivity": "com.tencent.mobileqq.activity.SplashActivity",


            "deviceName": "1b3129a9",  #华为：STF-AL00   #oppo:1b3129a9
            "noReset": True,  # 去掉页面弹窗，提升云效速度
            "skipServerInstallation" : 'true',  # 跳过安装、权限设置等操作(提升app运行速度),
            "skipDeviceInitialization": 'true',
            'automationName':'UiAutomator1',
            # "chromedriverExecutable": "/Users/xmly/Documents/chromedriver74"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        sleep(3)


