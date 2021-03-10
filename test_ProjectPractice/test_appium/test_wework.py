'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_wework.py
@time: 2021/3/5 11:10
@Email: Warron.wang
'''


import time

import pytest
from appium import webdriver   # pip install appium-python-client
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

from test_ProjectPractice.test_appium.test_swipe_find import *

class TestSign():
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

            # "deviceName": "T3Q6T16301006992",  # honor：T3Q6T16301006992   #oppo:1b3129a9
            "deviceName": "emulator-5554",  # honor：T3Q6T16301006992   #oppo:1b3129a9
            "noReset": True,  # 去掉页面弹窗，提升云效速度
            "skipServerInstallation": 'true',  # 跳过安装uiautomator2server等 服务
            "skipDeviceInitialization": 'true',  # 跳过设备的初始化
            "settings[waitForIdleTimeout]": 1, # settings 控制 动态页面的等待时长
            'automationName': 'UiAutomator1',
            'unicodeKeyboard': True,  # 使用unicode编码方式发送字符串
            'resetKeyboard': True,  # 将键盘隐藏起来
            # 'dontStopAppOnReset': "true"  # 运行前不停止app

        }
        # 客户端与appium服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()


    # 封装模拟页面滑动方法
    def swipe_find(self, text, num=3):
        for i in range(num):
            if i == num -1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次，未找到")
            self.driver.implicitly_wait(1)

            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到此元素")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3
                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)


    @pytest.mark.skip
    def test_sign(self):
        '''
        前提条件：已登录
        打卡用例：
        1、打开【企业微信】应用
        2、进入【工作台】
        3、点击【打卡】
        4、选择【外出打卡】tab
        5、点击【第N次打卡】
        6、验证【外出打卡成功】
        7、退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH, "//android.view.ViewGroup//*[@text='工作台']").click()
        # 滑动查找  目前是向下滑动两次，再向上查找，知道找到元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        print(self.driver.page_source) #打印当前页面结构
        time.sleep(2)
        # assert "外出打卡成功" in self.driver.page_source

        # 激活隐式等待
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")

    @pytest.mark.parametrize("username, mobilephone", [
        ('测试13', '13524631113'),
        # ('测试11', '13524631111')
    ])
    def test_addcontact(self, username, mobilephone):
        '''
        前提条件：已登录
        打卡用例：
        1、打开【企业微信】应用
        2、进入【通讯录】
        3、滑动页面查询【添加成员】并点击
        4、点击【手动输入添加】
        5、输入【姓名】、【手机号】，点击【保存】
        6、退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # 滑动查找  目前是向下滑动两次，再向上查找，知道找到元素
        # 方案一
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().text("添加成员").'
        #                                                 'instance(0));').click()
        # 方案二
        Add_locator = (MobileBy.XPATH, "//*[@text='添加成员']")
        swipe_up_search_element(self.driver, Add_locator)

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 需要通过同一个父节点获取子节点
        # 两种定位方法：
        # //*[contains(@text, '姓名')]/../*[@text='必填']
        # //*[contains(@text, '姓名')]/../android.widget.EditText
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']").send_keys(username)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys(mobilephone)
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(mobilephone)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 断言  添加成员成功toast
        time.sleep(1)
        # print(self.driver.page_source)
        # assert "外出打卡成功" in self.driver.page_source

        # 激活隐式等待
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")



    # 删除联系人
    def test_delcontact(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/igk").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='搜索']").send_keys("hogwarts_1")
        elelist = self.driver.find_elements(MobileBy.XPATH, "//*[@text='hogwarts_011']")
        # find_elements 方法返回的是一个列表 [element1, element2.....]
        if len(elelist) > 1:
            elelist[1].click()