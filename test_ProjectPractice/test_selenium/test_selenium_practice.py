'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_selenium_practice.py
@time: 2021/2/26 10:43
@Email: wei1.wang@ximalaya.com
'''
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestTmp():
    '''
    复用已有浏览器
    '''
    def setup_method(self, method):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver = webdriver.Chrome()
        self.vars = {}
        # self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def test_main_tmp(self):
        '''
        基于首页登录
        :return:
        '''
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()
        self.driver.find_element(By.XPATH, "//*[@id='corp_name']").send_keys("xxx")
        sleep(5)

    def test_login_tmp(self):
        '''
        基于浏览器复用后后的内容进行操作
        :return:
        '''
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

    def test_cookie_login(self):
        '''
        利用cookie进行登录
        :return:
        '''
        # 存入cookie
        # cookies = self.driver.get_cookies()
        # # print(cookies)
        # with open("tmp2.txt", "w", encoding="utf-8") as f:
        #     # 序列化
        #     # f.write(json.dumps(cookies)) 或者 下面的写法
        #     json.dump(cookies, f)

        # # 读取 cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("tmp2.txt", "r", encoding="utf-8") as f:
            # 反序列化
            # raw_cookie = f.read()  或者 下面的写法
            # cookies = json.loads(raw_cookie) 或者 下面的写法
            cookies = json.load(f)
        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)