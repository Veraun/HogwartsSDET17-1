'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: editPersonal_page.py.py
@time: 2021/3/9 23:52
@Email: Warron.Wang
'''
from appium.webdriver.common.mobileby import MobileBy

from test_ProjectPractice.test_appium.app_po.page.base_page import BasePage
from test_ProjectPractice.test_appium.app_po.page.personalDetail_page import PersonalDetailPage


class EditPersonalPage(BasePage):
    def edit_person(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='编辑成员']")
        return PersonalDetailPage(self.driver)