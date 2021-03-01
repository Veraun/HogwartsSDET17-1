'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: address_page.py
@time: 2021/3/1 17:12
@Email: wei1.wang@ximalaya.com
'''
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage():
    def __init__(self, driver):
        self.driver = driver

    def add_member(self):
        '''
        # 不可交互
        # 1.元素被遮挡：元素前面还有其他不可见元素
        # 2.元素有多个，需要人工挑选中合适的元素
        '''

        # 加入显示等待
        def wait_name(driver):
            self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[-1].click()
            eles = driver.find_elements(By.XPATH, "//*[@id='username']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_name)
        # 输入姓名
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("测试3")
        # 输入账号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("test03")
        # 输入手机号
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys("13524630003")
        # 点击保存
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()