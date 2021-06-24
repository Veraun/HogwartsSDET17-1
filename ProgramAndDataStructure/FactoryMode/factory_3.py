'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: factory_1.py
@time: 2021/6/9 15:19
@Email: Warron.Wang
'''
# 工厂方法

# 问题：如果多个公司都要封装工厂，比如：A,B,C...公司都要封装自己的工厂，就要封装n个工厂类
# 解决：可以使用抽象工厂解决问题，每个工厂类可以创建多个实例，比如：JsonParseRuleFactory可以创建A,B,C公司的实例.，请看factory_4.py


class Demo:
    def load(self, rule):
        parse = None
        # 根据不同的rule，创建不同的对象
        if "xml" == rule:
            # 省略 1000 行代码
            parse = XmlParse()
        elif "json" == rule:
            parse = JsonParseRuleFactory().create_parse()
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


# 相当于接口，用于规范各个工厂类
class IParseRuleFactory:
    def create_parse(self):
        raise ValueError()


# 工厂：把json的解析放到此工厂下面
class JsonParseRuleFactory(IParseRuleFactory):
    def create_parse(self):
        # 省略 1000 行代码
        return JsonParse()


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