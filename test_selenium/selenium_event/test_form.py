#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 18:54
# @Author  : Warren.wang
# @File    : test_form.py
# @Software: PyCharm
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
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

        # 定位"记住密码选择框"，并点击勾选
        '''
        方法有五种，当然方法1是无效错误的，所以才会有方法2-5
        方法1：直接定位元素后用.click()方法，但会报错
        方法2：直接使用JavaScript实现元素定位和动作执行
        方法3：先使用webdriver获取想要操作的元素，然后使用JavaScript执行操作
        方法4：使用鼠标事件ActionChains来操作
        方法5：页面中加了一个伪元素遮挡了原本的input元素，可以直接定位到伪元素上进行点击操作
        '''
        # 方法1：直接定位元素后用.click()方法，但会报错
        # self.driver.find_element_by_id("user_remember_me").click() 或
        # self.driver.find_element_by_xpath('//*[@id="user_remember_me"]').click()

        # 方法2：直接使用JavaScript实现元素定位和动作执行
        # self.driver.execute_script('return document.getElementById("user_remember_me").click()')

        # 方法3：先使用webdriver获取想要操作的元素，然后使用JavaScript执行操作
        # ele = self.driver.find_element_by_xpath('//*[@id="user_remember_me"]')
        # self.driver.execute_script("arguments[0].click();", ele)

        # # 方法4：使用鼠标事件ActionChains来操作
        # ele = self.driver.find_element_by_xpath('//*[@id="user_remember_me"]')
        # webdriver.ActionChains(self.driver).move_to_element(ele).click(ele).perform()

        # # 方法4：使用鼠标事件ActionChains来操作
        # action = ActionChains(self.driver)
        # ele = self.driver.find_element_by_xpath('//*[@id="user_remember_me"]')
        # action.click(ele).perform()

        # # 方法5：页面中加了一个伪元素遮挡了原本的input元素，可以直接定位到伪元素上进行点击操作
        self.driver.find_element_by_xpath('//*[@class="custom-control-label"]').click()


        # 点击提交按钮
        self.driver.find_element(By.XPATH,'//*[@id="new_user"]/div[4]/input').click()

