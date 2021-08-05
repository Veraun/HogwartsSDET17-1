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
    def load_yaml(path, key_words=""):
        datas = []
        if path != "":
            with open(path, encoding='utf-8') as f:
                datas = yaml.safe_load(f)
            if key_words == "":
                return datas
            else:
                return datas[key_words]
        return datas

# if __name__ == '__main__':
#     list_normal_data = Utils.load_yaml(r"../data/calendar/list.yml", "normal")
#     print(list_normal_data)
