#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 15:18
# @Author  : Warren.wang
# @File    : test_file.py
# @Software: PyCharm

'''
https://blog.csdn.net/weixin_34194379/article/details/93204792
'''
from time import sleep

from test_selenium.selenium_frame_window.base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id("stfile").send_keys("E:\\ban_about.jpg")
        sleep(3)
        print(self.driver.title)