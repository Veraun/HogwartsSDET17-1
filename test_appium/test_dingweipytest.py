'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_dingweipytest.py
@time: 2021/2/18 18:13
@Email: wei1.wang@ximalaya.com
'''
import pytest
from appium import webdriver


class TestDW():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['noReset'] = 'true'  # 去掉页面弹窗
        desired_caps['dontStopAppOnReset'] = 'true'  # 启动时不停止app(提升app运行速度)
        desired_caps['skipDeviceInitialization'] = 'true'  # 跳过安装、权限设置等操作(提升app运行速度)
        desired_caps['unicodeKeyBoard'] = 'true'  # case里输入如果有中文，需要设置
        desired_caps['resetKeyBoard'] = 'true'  # case里输入如果有中文，需要设置
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print("搜索测试用例")
        '''
        1. 打开雪球app
        2. 点击搜索输入框
        3. 向搜索输入框里面输入 "阿里巴巴"
        4. 在搜索框里选择 "阿里巴巴"，然后进行点击
        5. 获取 阿里巴巴 股价，并判断这只股价的价格>200
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/stockName" and @text="阿里巴巴"]').click()
        current_price = self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/current_price" and @text="270.83"]').text
        print(current_price)
        assert current_price > 200

if __name__ == '__main__':
    pytest.main()