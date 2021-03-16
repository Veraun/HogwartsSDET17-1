'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_grid.py
@time: 2021/3/16 20:04
@Email: Warron.Wang
'''

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

# 脚本运行对node进行分发
class TestGrid:
    def test_grid(self):
        # hub地址
        hub_url = "http://127.0.0.1:4444/wd/hub"
        capability = DesiredCapabilities.CHROME.copy()
        for i in range(1,5):
            driver = Remote(command_executor=hub_url, desired_capabilities=capability)
            driver.get("https://ceshiren.com/")