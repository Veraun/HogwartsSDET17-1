'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: main_page.py
@time: 2021/3/1 17:09
@Email: wei1.wang@ximalaya.com
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_ProjectPractice.test_selenium.address_page.address_page import AddressPage


class MainPage:
    def __init__(self):
        # 声明 chrome的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        # self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def goto_address(self):
        # 切换到通讯录
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        return AddressPage(self.driver)