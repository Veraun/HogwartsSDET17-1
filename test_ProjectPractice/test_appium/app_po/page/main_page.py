'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: main_page.py
@time: 2021/3/7 16:06
@Email: Warron.Wang
'''

# 主页
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from test_ProjectPractice.test_appium.app_po.page.addresslist_page import AddressListPage
from test_ProjectPractice.test_appium.app_po.page.base_page import BasePage


class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_addresslist(self):
        # 点击 通讯录
        self.find(*self.addresslist_element).click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)

