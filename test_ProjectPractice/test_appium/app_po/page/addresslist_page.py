'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: addresslist_page.py
@time: 2021/3/9 22:34
@Email: Warron.Wang
'''
from appium.webdriver.common.mobileby import MobileBy

from test_ProjectPractice.test_appium.app_po.page.addcontact_page import AddContactPage
from test_ProjectPractice.test_appium.app_po.page.base_page import BasePage
from test_ProjectPractice.test_appium.app_po.page.search_page import SearchPage


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    def click_addcontact(self):
        element = self.swipe_find("添加成员")
        element.click()
        return AddContactPage(self.driver)

    def goto_search(self):
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/igk")
        return SearchPage(self.driver)