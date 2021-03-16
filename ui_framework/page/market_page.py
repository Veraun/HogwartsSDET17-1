'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: market_page.py
@time: 2021/3/15 09:52
@Email: Warron.Wang
'''
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from ui_framework.page.base_page import BasePage
from ui_framework.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        # self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")

        # with open("../page/market_page.yml", "r", encoding="utf-8") as f:
        #     function = yaml.load(f)
        # steps = function["goto_search"]
        # for step in steps:
        #     if step.get("action") == "find_and_click":
        #         self.find_and_click(step.get("locator"), step.get("value"))
        self.parse("../page/market_page.yml", "goto_search")
        return SearchPage(self.driver)
