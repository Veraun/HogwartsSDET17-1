#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 15:17
# @Author  : Warren.wang
# @File    : test_alert.py
# @Software: PyCharm
'''
常用方法：
页面操作会遇到js所生成的alert、confirm以及prompt弹框。
可以使用switch_to.alert()方法定位，然后使用text/accept/dismiss/send_keys等方法进行操作。
操作alert常用方法：
switch_to.alert()：获取当前页面上的警告框
text:返回alert、confirm以及prompt中文字信息
accept()：接受现有警告框
dismiss()：解散现有警告框
send_keys(keysToSend)：发送文本至警告框
keyToSend：将文本发送至警告框
'''
from time import sleep

from selenium.webdriver import ActionChains

from test_selenium.selenium_frame_window.base import Base


class TestAlert(Base):
    def test_alert(self):
        '''
        打开网页 https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        操作窗口右侧页面，将元素1拖拽到元素2
        这时候会有一个alert弹框，点击弹框中的"确定"
        然后再按"点击运行"
        关闭网页
        :return:
        '''
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #1切换到frame下
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        #2拖拽元素
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop)
        action.perform()

        print("点击alert 确认")
        self.driver.switch_to.alert.accept() #接受现有警告框

        #3.切换到默认frame
        self.driver.switch_to.default_content()

        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)