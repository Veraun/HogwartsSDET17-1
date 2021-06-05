'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_data_5.py
@time: 2021/5/26 11:13
@Email: Warron.Wang
'''
import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def testdemo(self, env):
        if "test" in env:
            print("这是测试环境")
            print(env)
            print("测试环境的ip是：",env["test"])
        elif "dev" in env:
            print("这是开发环境")
            print(env)
            print("开发环境的ip是：",env["dev"])

    def test_yaml(self):
        print(yaml.safe_load(open("./env.yml")))
