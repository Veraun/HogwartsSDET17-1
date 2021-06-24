'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: factory_2.py
@time: 2021/6/9 15:35
@Email: Warron.Wang
'''

# 简单工厂模式

# 问题：factory_2.py中，简单工厂不能解决创建实例的代码可能很复杂的问题，即使迁移了简单工厂中，复杂的创建过程依旧存在
# 解决：使用工厂方法，把创建过程封装到工厂类，请看factory_3.py

class Demo:
    def load(self, rule):
        parse = ParseRuleFactory().create_parse(rule)
        # 调用对象的方法进行操作
        parse.parse()


# 简单工厂类：用于实例的创建，根据rule创建不同的实例。本质就是把Demo中原来创建实例的代码，给迁移过来
class ParseRuleFactory:
    def create_parse(self, rule):
        parse = None
        # 根据不同的rule，创建不同的对象
        if "xml" == rule:
            parse = XmlParse()
        elif "json" == rule:
            parse = JsonParse()
        elif "excel" == rule:
            parse = ExcelParse()
        elif "csv" == rule:
            parse = CsvParse()
        else:
            parse = OtherParse()
        return parse


# 相当于接口，用于规范各个解析类
# 每个解析类都要实现parse方法，否则在调用的时候就会报错
class IParse:
    def parse(self):
        raise ValueError


class XmlParse(IParse):
    def parse(self):
        print("XmlParse")


class JsonParse(IParse):
    def parse(self):
        print("JsonParse")


class ExcelParse(IParse):
    def parse(self):
        print("ExcelParse")


class CsvParse(IParse):
    def parse(self):
        print("CsvParse")


class OtherParse(IParse):
    def parse(self):
        print("OtherParse")


if __name__ == '__main__':
    Demo().load("json")
    Demo().load("excel")