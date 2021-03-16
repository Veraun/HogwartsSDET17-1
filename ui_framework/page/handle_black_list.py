'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: handle_black_list.py
@time: 2021/3/14 15:53
@Email: Warron.Wang
'''
import allure
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from ui_framework.page.logger import log, log_init


def handle_black(func):
    def wrapper(*args, **kwargs):
        black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']
        # args[0]相当于self
        instance = args[0]
        try:
            print(f"进入装饰器,{func.__name__}")
            log_init()
            log.debug("新定位元素是：%s", args[2])
            obj = func(*args, **kwargs)
            return obj
        except Exception:
            instance.screenshot()
            with open("./tmp.png", "rb") as f:
                allure.attach(f.read(), attachment_type=allure.attachment_type.PNG)
            # allure.attach(instance.screenshot(), attachment_type=allure.attachment_type.PNG)
            for ele_xpath in black_list:
                # 用火眼金睛去看，妖魔鬼怪是否存在
                eles = instance.finds(By.XPATH, ele_xpath)
                # 妖魔鬼怪出现了，需要斩杀
                if len(eles) > 0:
                    eles[0].click()
                return func(*args, **kwargs)
            print("出来装饰器")
    return wrapper