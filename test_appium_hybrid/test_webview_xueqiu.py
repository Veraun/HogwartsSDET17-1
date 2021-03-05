'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_webview_apidemo.py
@time: 2021/2/23 17:52
@Email: Warron.wang
'''
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        des_caps = {
            "platformName": "android",
            "platformVersion": "6.0",
            "appPackage":"com.xueqiu.android",
            "appActivity":"com.xueqiu.android.common.MainActivity",
            # "browserName": "Browser",  # 被测浏览器
            # "deviceName": "emulator-5554",
            "deviceName": "192.168.56.102:5555",
            "noReset": True,  # 去掉页面弹窗，提升云效速度
            "skipServerInstallation" : 'true',  # 跳过安装、权限设置等操作(提升app运行速度)
            "chromedriverExecutable": "/Users/xmly/Documents/chromedriver74"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        # 原生
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click() # 点击交易
        A_locator = (MobileBy.XPATH, "//*[@id='app']/div/div/div/ul/li[1]/div[2]/h1")
        print(self.driver.contexts)
        # 切换上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        # webview
        print(self.driver.window_handles)
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(A_locator)) # 点击'A股开户'
        self.driver.find_element(*A_locator).click()

        # 切换window
        print(self.driver.window_handles)
        kaihu_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(kaihu_window)

        # 输入用户名和验证码，点击立即开户
        # 增加显示等待
        phonenumber_locator = (MobileBy.ID, "phone-number")
        WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable(phonenumber_locator))
        self.driver.find_element(*phonenumber_locator).send_keys("13524631949")
        self.driver.find_element(MobileBy.ID, "code").send_keys("123456")
        self.driver.find_element(MobileBy.CSS_SELECTOR, "body > div > div > div.form-wrap > div > div.btn-submit").click()



