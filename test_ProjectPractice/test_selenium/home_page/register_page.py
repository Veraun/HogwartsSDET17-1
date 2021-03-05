'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: register_page.py
@time: 2021/3/1 15:49
@Email: Warron.wang
'''
from selenium.webdriver.common.by import By


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def register(self):
        self.driver.find_element(By.XPATH, "//*[@id='corp_name']").send_keys("xxx")
