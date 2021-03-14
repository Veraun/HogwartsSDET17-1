'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: handle_black_list.py
@time: 2021/3/14 15:53
@Email: Warron.Wang
'''

from appium.webdriver.common.mobileby import MobileBy

from selenium.common.exceptions import NoSuchElementException


def handle_black(func):
    def wrapper(*args, **kwargs):
        black_list = ['//*[@resource-id="com.xueqiu.android:id/iv_close"]']
        # 相当于self
        instance = args[0]
        try:
            print(f"进入装饰器,{func.__name__}")
            obj = func(*args, **kwargs)
            if len(obj) == 0:
                raise NoSuchElementException("未找到此元素")
            return obj
        except Exception:
            for ele_xpath in black_list:
                # 用火眼金睛去看，妖魔鬼怪是否存在
                eles = instance.finds(MobileBy.XPATH, ele_xpath)
                # 妖魔鬼怪出现了，需要斩杀
                if len(eles) > 0:
                    eles[0].click()
                return func(*args, **kwargs)
            print("出来装饰器")
    return wrapper