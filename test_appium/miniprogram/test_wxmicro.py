'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_wxmicro.py
@time: 2021/3/19 16:39
@Email: Warron.Wang
'''
from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

'''
微信小程序
'''

class TestWXMicro:
    def setup(self):
        caps = {}
        caps["platformName"] = "android",
        caps["deviceName"] = "测试人",
        caps["appPackage"] = "com.tencent.mm",
        caps["appActivity"] = "com.tencent.mm.ui.LauncherUI",
        caps["noReset"] = True,
        caps["unicodeKeyboard"] = True,
        caps["resetKeyboard"] = True,
        # 第一步，设置chromedriver正确版本
        caps["chromedriverExecutable"] = "/Users/xmly/Documents/mychromedriver/all/chromedriver74"
        # 第二步,设置chrome option传递给chromedriver
        caps["chromeOptions"] = {
            "androidProcess": "com.tencent.mm.appbrand0"
        }

        # 第三步，使用adb proxy解决fix chromedriver的bug
        caps["adbPort"] = 5038

        # 客户端与appium服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

        self.driver.find_element(By.XPATH, "//*[@text='通讯录']")
        self.driver.implicitly_wait(10)

    def test_search(self):
        # 原生自动化测试
        size = self.driver.get_window_size()
        self.driver.swipe(size['width']*0.5,size['height']*0.8,size['width']*0.5,size['height']*0.3)
        self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').click()
        self.driver.find_element(By.XPATH, "//*[@text='取消']")
        self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys("雪球")
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button')
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
        self.driver.find_element(By.XPATH, "//*[@text='自选']")
        print(self.driver.contexts)


        # 进入webview，切入到小程序的上下文
        self.driver.switch_to.context("WEBVIEW_xweb")
        self.driver.implicitly_wait(10)
        self.find_top_window()

        # css定位
        self.driver.find_element(By.CSS_SELECTOR, "[src*=stock_add]").click()
        # 等待新窗口
        WebDriverWait(self.driver).until(lambda x: len(self.driver.window_handles) > 2)
        self.find_top_window()
        self.driver.find_element(By.CSS_SELECTOR, "._input").click()
        # 输入
        self.driver.switch_to.context("NATIVE_APP")
        ActionChains(self.driver).send_keys("alibaba").perform()
        # 点击
        self.driver.switch_to.context("WEBVIEW_xweb")
        self.driver.find_element(By.CSS_SELECTOR, ".stock_item")
        self.driver.find_element(By.CSS_SELECTOR, ".stock_item").click()

    # 在小程序里，找可视化窗口
    def find_top_window(self):
        # 遍历window窗口
        for window in self.driver.window_handles:
            print(window)
            if ":VISIBLE" in self.driver.title:
                # 判断哪个是可视化的
                print("find")
                print(self.driver.title)
                # return True
            else:
                self.driver.switch_to.window(window)
        # return False