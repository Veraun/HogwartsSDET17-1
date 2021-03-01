'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: login_page.py
@time: 2021/3/1 15:49
@Email: wei1.wang@ximalaya.com
'''
from selenium.webdriver.common.by import By

from test_ProjectPractice.test_selenium.home_page.register_page import RegisterPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def scan(self):
        pass

    def goto_register(self):
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()
        return RegisterPage(self.driver)

