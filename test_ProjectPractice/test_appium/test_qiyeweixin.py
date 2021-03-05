'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_qiyeweixin.py
@time: 2021/3/2 11:10
@Email: Warron.wang
'''


import time

import pytest
from appium import webdriver   # pip install appium-python-client
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
    def setup(self):
        des_caps = {
            "platformName": "android",
            "platformVersion": "6.0.1",

            # 获取appPackage和appActivity最佳命令
            # adb logcat ActivityManager:I | grep "cmp"

            # 通讯录
            # "appPackage":"com.android.contacts",
            # "appActivity":"com.android.contacts.activities.PeopleActivity",

            # 企业微信
            "appPackage": "com.tencent.wework",
            "appActivity": "com.tencent.wework.launch.LaunchSplashActivity",

            # 个人微信
            # "appPackage": "com.tencent.mm",
            # "appActivity": "com.tencent.mm.ui.LauncherUI",

            # qq
            # "appPackage": "om.tencent.mobileqq",
            # "appActivity": "com.tencent.mobileqq.activity.SplashActivity",

            "deviceName": "T3Q6T16301006992",  # honor：T3Q6T16301006992   #oppo:1b3129a9
            "noReset": True,  # 去掉页面弹窗，提升云效速度
            "skipServerInstallation": 'true',  # 跳过安装、权限设置等操作(提升app运行速度),
            "skipDeviceInitialization": 'true',
            'automationName': 'UiAutomator1',
        }

        # 客户端与appium服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        # time.sleep(5)
        el1 = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/igk")
        el1.click()
        el2 = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gy9")
        el2.send_keys("王")
        # el3 = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gy9")

