'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_dingweipytest.py
@time: 2021/2/18 18:13
@Email: Warron.wang
'''
import time

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW():
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

    @pytest.mark.skip
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
        current_price = float(self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/current_price" and @text="270.83"]').text)
        print(current_price)
        assert current_price > 200

    @pytest.mark.skip
    def test_attr(self):
        '''
        打开 【雪球】应用
        定位首页的搜索框
        判断搜索框是否可用，并查看搜索框name属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入：alibaba
        判断【阿里巴巴】是否可见
        如果可见，打印"搜索成功"点击；如果不可见，打印"搜索失败"
        :return:
        '''
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(element.is_enabled())
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            #alibaba_element.is_displayed()
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == "true":
                print("搜索成功")
            else:
                print("搜索失败")

    @pytest.mark.skip
    def test_touchaction(self):
        action = TouchAction(self.driver)
        #1获取坐标点，进行滑动  不推荐
        # action.press(x=731, y=2083).wait(300).move_to(x=731, y=484).release().perform()

        #2获取坐标点，进行滑动  推荐
        # print(self.driver.get_window_rect())
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height* 4/5)
        y_end = int(height* 1/5)
        action.press(x=x1, y=y_start).wait(300).move_to(x=x1, y=y_end).release().perform()

    @pytest.mark.skip
    def test_xpath(self):
        '''
        元素定位高阶用法
        :return:
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # self.driver.find_element_by_xpath('//*[@resource-id="com.xueqiu.android:id/stockName" and @text="阿里巴巴"]').click()
        self.driver.find_element_by_xpath('//*[@text="BABA"]').click()
        #获取股票价格
        current_price = self.driver.find_element_by_xpath('//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        print(f"当前09988股票对应的股票价格是：{current_price}")
        assert float(current_price) > 200

    @pytest.mark.skip
    def test_myinfo(self):
        '''
        使用：find_element_by_android_uiautomator定位
        1.点击 我的，进入个人信息页面
        2.点击登录，进入到登录页面
        3.输入用户名和密码
        4.点击登录
        :return:
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("wiki")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("wiki123")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")')
        # self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelect(text("股票"))')

    @pytest.mark.skip
    def test_scroll_find_element(self):
        '''
        在页面实现滚动查找指定元素，如：轻金融
        :return:
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("轻金融").'
                                                        'instance(0));').click()
        time.sleep(3)

if __name__ == '__main__':
    pytest.main()