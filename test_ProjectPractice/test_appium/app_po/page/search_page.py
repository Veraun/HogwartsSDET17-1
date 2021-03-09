'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: search_page.py
@time: 2021/3/9 23:56
@Email: Warron.Wang
'''
from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from test_ProjectPractice.test_appium.app_po.page.base_page import BasePage
from test_ProjectPractice.test_appium.app_po.page.personal_page import PersonalPage


class SearchPage(BasePage):
    def search_and_click(self, search_content):
        self.find_and_sendKeys(MobileBy.XPATH, "//*[@text='搜索']", search_content)
        sleep(1)
        elements = self.finds(MobileBy.XPATH, f"//*[@text='{search_content}']")
        if len(elements) > 1:
            elements[-1].click()
            return len(elements), PersonalPage(self.driver)
        else:
            raise NoSuchElementException(f"没有找到匹配的元素：{search_content}")

    def search(self, search_content):
        elements = self.finds(MobileBy.XPATH, f"//*[@text='{search_content}']")
        return len(elements)