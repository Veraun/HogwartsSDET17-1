#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 19:06
# @Author  : Warren.wang
# @File    : test_demo.py
# @Software: PyCharm

import selenium
from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")