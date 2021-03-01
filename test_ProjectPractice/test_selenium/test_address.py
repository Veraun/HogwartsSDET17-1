'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_address.py
@time: 2021/3/1 10:02
@Email: wei1.wang@ximalaya.com
'''

import json

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait


class TestTmp():
    '''
    复用已有浏览器
    '''
    def setup_method(self, method):
        # 声明 chrome的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        # self.driver = webdriver.Chrome()
        self.vars = {}
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    # @pytest.mark.skip
    def test_login_with_debug(self):
        '''
        基于浏览器复用后后的内容进行操作
        :return:
        '''
        # self.driver.get("https://www.baidu.com/")
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 切换到通讯录
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        sleep(1)
        '''
        # 不可交互
        # 1.元素被遮挡：元素前面还有其他不可见元素
        # 2.元素有多个，需要人工挑选中合适的元素
        '''
        # 加入显示等待
        def wait_name(driver):
            self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")[1].click()
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
