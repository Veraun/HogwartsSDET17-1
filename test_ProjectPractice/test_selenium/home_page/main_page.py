'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: main_page.py
@time: 2021/3/1 15:48
@Email: wei1.wang@ximalaya.com
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_ProjectPractice.test_selenium.home_page.login_page import LoginPage
from test_ProjectPractice.test_selenium.home_page.register_page import RegisterPage


class MainPage:
    def __init__(self):
        # 声明 chrome的参数
        # chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        # chrome_arg.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/")

    def goto_register(self):
        '''
        从首页进入注册页
        怎么将driver传过去？：哪里用哪里传
        何时传？：调用方法时传
        :return:
        '''
        self.driver.find_element(By.XPATH, "//*[@class='index_head_info_pCDownloadBtn']").click()
        # 方便链式调用
        # 将类初始化成对象
        return RegisterPage(self.driver)

    def goto_login(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
        return LoginPage(self.driver)

    def goto_download(self):
        pass