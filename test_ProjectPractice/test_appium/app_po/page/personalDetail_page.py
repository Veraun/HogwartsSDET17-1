'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: personalDetail_page.py
@time: 2021/3/9 23:53
@Email: Warron.Wang
'''
from appium.webdriver.common.mobileby import MobileBy

from test_ProjectPractice.test_appium.app_po.page.base_page import BasePage


class PersonalDetailPage(BasePage):
    def edit_name(self):
        pass

    def del_contact(self):
        self.swipe_find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.find_and_click(MobileBy.XPATH, "//*[@text='确定']")