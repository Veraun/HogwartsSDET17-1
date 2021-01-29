#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 15:37
# @Author  : Warren.wang
# @File    : test_yaml.py
# @Software: PyCharm
import yaml


def test_yaml():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        print(datas["add"]["datas"])