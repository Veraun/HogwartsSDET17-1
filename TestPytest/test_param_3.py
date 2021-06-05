'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_param_3.py
@time: 2021/5/25 19:00
@Email: Warron.Wang
'''

import pytest

class TestData:
    @pytest.mark.parametrize("a,b", [
        (10,20),
        (10,5),
        (3,9)
    ])
    def test_data(self, a, b):
        print(a+b)


    @pytest.mark.parametrize(("a","b"), [
        [10,1],
        [10,1],
        [10,1]

    ])
    def test_data_1(self, a, b):
        print(a+b)


    @pytest.mark.parametrize(["a","b"], [
        (10,20),
        (10,5),
        (3,9)
    ])
    def test_data_2(self, a, b):
        print(a+b)
