#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/8 10:07
# @Author  : Warren.wang
# @File    : test_frame.py
# @Software: PyCharm
'''
web自动化中，如果一个元素定位不到，很大可能实在frame中。

什么是frame？
frame是html中的框架，在html中，所谓的框架就是可以在同一个浏览器中显示不止一个页面
基于html框架，又分为垂直框架和水平框架(cols,rows)

Frame分类
包含：frameset、frame、iframe
frameset和普通标签一样，不影响定位
frame和iframe定位类似。selenium有一组方法对frame进行操作

存在两种：嵌套和非嵌套的
多frame切换
switch_to.frame() #根据元素id或index切换frame
switch_to.default_content()  #切换到默认frame
switch_to.parent_frame()  #切换到父级frame

处理未嵌套的iframe
driver.switch_to_frame("frame的id")
driver.switch_to_frame("frame - index") #frame无id时根据索引来处理，索引从0开始

处理嵌套的iframe
对于嵌套的先进入到iframe的父节点，再进入子节点，然后可以对子节点里面的对象进行处理和操作
driver.switch_to_frame("父节点")
driver.switch_to_frame("子节点")
'''
from test_selenium.selenium_frame_window.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        #切换到frame里
        # self.driver.switch_to_frame("iframeResult")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        #从frame切回:以下二选一
        # self.driver.switch_to.parent_frame() #切换到父级frame
        self.driver.switch_to.default_content()  #切换到默认frame

        print(self.driver.find_element_by_id("submitBTN").text)
