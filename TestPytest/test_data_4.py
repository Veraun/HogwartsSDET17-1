'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_data_4.py
@time: 2021/5/26 09:19
@Email: Warron.Wang
'''

import pytest, yaml

class TestData:
    @pytest.mark.parametrize(("a","b"), yaml.safe_load(open("./data.yaml")))
    def test_data(self, a, b):
        print(a+b)
