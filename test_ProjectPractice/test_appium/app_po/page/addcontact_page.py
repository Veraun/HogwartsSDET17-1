'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: addcontact_page.py
@time: 2021/3/9 22:35
@Email: Warron.Wang
'''

# 添加成员页面
from appium.webdriver.common.mobileby import MobileBy

from test_ProjectPractice.test_appium.app_po.page.base_page import BasePage
from test_ProjectPractice.test_appium.app_po.page.editcontact_page import EditContactPage


class AddContactPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    def addcontact_menual(self):
        # 手动输入添加
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return EditContactPage(self.driver)