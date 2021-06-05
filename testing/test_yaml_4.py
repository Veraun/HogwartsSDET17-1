#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 15:37
# @Author  : Warren.wang
# @File    : test_yaml_4.py
# @Software: PyCharm
import yaml


def test_yaml():
    with open("./datas/test.yml", encoding="utf-8") as f:
        # 将yaml数据流转化为python对象
        datas = yaml.safe_load(f)
        print(datas)
        # print(datas["add"]["datas"])