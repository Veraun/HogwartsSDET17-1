'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: utils.py
@time: 2021/7/12 16:20
@Email: Warron.Wang
'''
import yaml


class Utils:
    @staticmethod
    def load_yaml(cls, path):
        with open(path, encoding='utf-8') as f:
            cls.all_datas = yaml.safe_load(f)
        return cls.all_datas
