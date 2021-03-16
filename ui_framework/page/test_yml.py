'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_yml.py
@time: 2021/3/15 16:52
@Email: Warron.Wang
'''
import yaml

def test_y():
    with open("../page/main_page.yml", "r", encoding="utf-8") as f:
        function = yaml.load(f)
    steps = function.get("goto_market")
    for step in steps:
        print(step.get("locator"))
    print(steps)