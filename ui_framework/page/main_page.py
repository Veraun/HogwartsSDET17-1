'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: main_page.py
@time: 2021/3/12 09:06
@Email: Warron.Wang
'''
import yaml
from appium.webdriver.common.mobileby import MobileBy

from ui_framework.page.base_page import BasePage
from ui_framework.page.market_page import MarketPage


class MainPage(BasePage):
    # 进入行情

    def goto_market(self):
        # self.find_and_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        # self.find_and_click(MobileBy.XPATH, "//*[@text='行情']")

        # with open("../page/main_page.yml", "r", encoding="utf-8") as f:
        #     function = yaml.load(f)
        # steps = function["goto_market"]
        # for step in steps:
        #     if step.get("action") == "find_and_click":
        #         self.find_and_click(step.get("locator"), step.get("value"))
        self.parse("../page/main_page.yml", "goto_market")
        return MarketPage(self.driver)