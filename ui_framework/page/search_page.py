'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: search_page.py
@time: 2021/3/15 09:52
@Email: Warron.Wang
'''
import yaml
from appium.webdriver.common.mobileby import MobileBy

from ui_framework.page.base_page import BasePage


class SearchPage(BasePage):
    def search(self):
        # self.find_and_sendKeys(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']", "alibaba")

        # with open("../page/search_page.yml", "r", encoding="utf-8") as f:
        #     function = yaml.load(f)
        # steps = function["search"]
        # for step in steps:
        #     if step.get("action") == "find_and_click":
        #         self.find_and_click(step.get("locator"), step.get("value"))
        #     elif step.get("action") == "find_and_sendKeys":
        #         self.find_and_sendKeys(step.get("locator"), step.get("value"), step.get("text"))
        self.parse("../page/search_page.yml", "search")
