'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_swipe_find.py
@time: 2021/3/5 15:48
@Email: Warron.Wang
'''

'''
问题：如何封装滑动查找？（swipe TouchAction）,如何封装一个边滑动边查找函数？

思路：
（1）需要三个参数：deiver驱动对象、外层元素对象、要点击的文本内容
（2）location获取左上角坐标点
（3）size获取外层长宽
（4）得出单页面滑动的起始点和终止点位置（90%、10%）
（5）通过while True一直滑动，直到找到要点击的文本内容
'''

# 定义加滑动边查找的方法
def swipe_find(driver, element, location):
    # 获取滑动的元素坐标点
    lc = element.location
    # 获取滑动元素的大小
    size = element.size
    # 初始化元素坐标点的值
    x = lc['x']
    y = lc['y']
    w = size['width']
    h = size['height']
    startx = x + w * 0.9
    starty = y + h/2
    endx = x + w * 0.1
    while True:
        page = driver.page_source   # 获取的是整个app页面的信息
        try:
            driver.find_element(*location).click()  # 点击对应的元素信息
            return True
        except Exception as e:
            driver.swipe(startx, starty, endx, starty, duration=2000)
        if driver.page_source == page:
            print("已经滑动到最后页面，没有找到对应的频道信息!")
            return False


def swipe_up_search_element(driver,ele):
    #向上滑动后，寻找到一个元素后实现自动点击
    size = driver.get_window_size()
    x1 = size['width'] * 0.5
    y1 = size['height'] * 0.25
    y2 = size['height'] * 0.75
    i = 0
    while i < 20 :
        try:
            driver.find_element(*ele).click()  # 点击对应的元素信息
            break
        except Exception as e:
            driver.swipe(x1,y2,x1,y1)
            i = i+1
