'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: main_page.py
@time: 2021/3/12 09:06
@Email: Warron.Wang
'''
from appium.webdriver.common.mobileby import MobileBy

from ui_framework.page.base_page import BasePage


class MainPage(BasePage):
    # 进入行情
    market_element = (MobileBy.XPATH, "//*[@text='行情']")

    def goto_market(self):
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        self.find_and_click(*self.market_element)
        self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")
        self.find_and_sendKeys(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']", "alibaba")
        # return AddressListPage(self.driver)