'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: base_page.py
@time: 2021/3/12 09:06
@Email: Warron.Wang
'''


# 基类,初始化driver,find,finds,swipe_find等

import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import exceptions
from selenium.common.exceptions import NoSuchElementException

class BasePage:
    logging.basicConfig(level=logging.INFO, filename="../logs/app.log",
                        format="[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]", filemode="a",
                        datefmt="'%Y-%m-%d %I:%M:%S %p'")

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def black(self, func):
        black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']

        def wrapper(*args, **kwargs):
            try:
                print(f"进入装饰器,{func.__name__}")
                obj = func(*args, **kwargs)
                if len(obj) == 0:
                    raise NoSuchElementException("未找到此元素")
                return obj
            except exceptions :
                for ele_xpath in black_list:
                    # 用火眼金睛去看，妖魔鬼怪是否存在
                    eles = self.finds(MobileBy.XPATH, ele_xpath)
                    # 妖魔鬼怪出现了，需要斩杀
                    if len(eles) > 0:
                        eles[0].click()
                    return func(*args, **kwargs)
                print("出来装饰器")

        return wrapper

    @black
    def find_new(self, locator, value):
        logging.info("find")
        logging.info("定位方法是:%s,定位元素是：%s", locator, value)
        return self.driver.find_element(locator, value)

    def find_old(self, locator, value):
        black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']
        try:
            logging.info("find")
            logging.info("定位方法是:%s,定位元素是：%s", locator, value)
            return self.driver.find_element(locator, value)
        except Exception:
            # 取出所有的妖魔鬼怪，在这里一一进行处理
            for ele_xpath in black_list:
                # 用火眼金睛去看，妖魔鬼怪是否存在
                eles = self.finds(MobileBy.XPATH, ele_xpath)
                # 妖魔鬼怪出现了，需要斩杀
                if len(eles) > 0:
                    eles[0].click()
                    return self.find_old(locator, value)

    def finds(self, locator, value):
        logging.info("finds")
        # logging.info(locator, value)
        logging.info("定位方法是:%s,定位元素是：%s", locator, value)
        return self.driver.find_elements(locator, value)

    def find_and_click(self, locator, value):
        logging.info("find and click")
        logging.info("定位方法是:%s,定位元素是：%s", locator, value)
        # self.driver.find_element(locator, value).click()
        self.find_new(locator, value).click()

    def find_and_sendKeys(self, locator, value, text):
        logging.info("定位方法是:%s,定位元素是：%s,文本输入的是：%s", locator, value, text)
        return self.driver.find_element(locator, value).send_keys(text)

    def swip(self):
        size = self.driver.get_window_size()
        width = size.get('width')
        height = size.get('height')
        start_x = width / 2
        start_y = height * 0.8
        end_x = start_x
        end_y = height * 0.3
        self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def swipe_find(self, locator, value, num=3):
        for i in range(num):
            if i == num - 1:
                logging.info("set implicitly_wait :5")
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次， 未找到。")
            logging.info("set implicitly_wait :1")
            self.driver.implicitly_wait(1)
            try:
                # element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                element = self.driver.find_element(locator, value)
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                self.swip()
