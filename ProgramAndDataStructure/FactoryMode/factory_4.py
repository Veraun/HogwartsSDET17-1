'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: factory_1.py
@time: 2021/6/9 15:19
@Email: Warron.Wang
'''
# 抽象工厂方法


class Demo:
    def load(self, rule):
        parse = None
        # 根据不同的rule，创建不同的对象
        if "xml" == rule:
            # 省略 1000 行代码
            parse = XmlParse()
        elif "json" == rule:
            parse = JsonParseRuleFactory().a_create_parse()
        elif "excel" == rule:
            # 省略 1000 行代码
            parse = ExcelParse()
        elif "csv" == rule:
            # 省略 1000 行代码
            parse = CsvParse()
        else:
            parse = OtherParse()
        # 调用对象的方法进行操作
        parse.parse()


# 一个工厂类，可以生成多个公司的解析方法
class IParseRuleFactory:
    def a_create_parse(self):
        raise ValueError()

    def b_create_parse(self):
        raise ValueError()

    def c_create_parse(self):
        raise ValueError()


# 实现的时候，一个工厂类就可以生成多个公司的实例
class JsonParseRuleFactory(IParseRuleFactory):
    def a_create_parse(self):
        '''

        :return:
        '''

    def b_create_parse(self):
        '''

        :return:
        '''

    def c_create_parse(self):
        '''

        :return:
        '''


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