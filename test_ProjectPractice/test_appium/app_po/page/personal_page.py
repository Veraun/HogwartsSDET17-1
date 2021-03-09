'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: personal_page.py.py
@time: 2021/3/9 23:54
@Email: Warron.Wang
'''
from appium.webdriver.common.mobileby import MobileBy

from test_ProjectPractice.test_appium.app_po.page.base_page import BasePage
from test_ProjectPractice.test_appium.app_po.page.editPersonal_page import EditPersonalPage


class PersonalPage(BasePage):
    def click_more(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='个人信息']/../../../../..//*[@class='android.widget.RelativeLayout']")
        return EditPersonalPage(self.driver)