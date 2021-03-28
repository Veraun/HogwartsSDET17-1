#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 19:06
# @Author  : Warren.wang
# @File    : test_contact.py
# @Software: PyCharm
'''
http://npm.taobao.org/mirrors/chromedriver
mac系统：
1.一定要将chromedriver放在/usr/local/bin
2.然后再vim ~/.bash_profile，export PATH=$PATH:/usr/local/bin
'''

from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")