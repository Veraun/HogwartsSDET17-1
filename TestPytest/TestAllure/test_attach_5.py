'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_attach_5.py
@time: 2021/5/28 11:02
@Email: Warron.Wang
'''
import allure


def test_attach_text():
    allure.attach("这是一个纯文本哈哈",attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach('''<body>这是一段html body块代码</body>''', name="html测试块", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file("/Users/xmly/Desktop/coupon.jpg", name="这是一张图片", attachment_type=allure.attachment_type.JPG)


def test_attach_video():
    allure.attach.file("/Users/xmly/Desktop/tmp.mp4", name="这是一个视频", attachment_type=allure.attachment_type.MP4)