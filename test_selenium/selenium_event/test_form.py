#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 18:54
# @Author  : Warren.wang
# @File    : test_form.py
# @Software: PyCharm
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        user_id = self.driver.find_element_by_id("user_login")
        user_id.send_keys("wiki918")
        print(user_id.get_attribute("value"))
        passwd = self.driver.find_element_by_id("user_password")
        passwd.send_keys("@*3614358wang")
        print(passwd.get_attribute("value"))
        # self.driver.find_element_by_id("user_remember_me").click()
        # self.driver.find_element(By.XPATH,'//*[@id="user_remember_me"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="new_user"]/div[4]/input').click()

