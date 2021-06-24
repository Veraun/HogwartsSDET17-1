'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: factory_1.py
@time: 2021/6/9 15:19
@Email: Warron.Wang
'''

# Demo用于加载不同的文件，对不同的文件做不同的处理
# 问题：如果创建对象的代码比较多，可能还会创建 text，md、yml等等
# 简单工厂解决：把对象的创建移动到其他类中，load方法就会很简洁，请看factory_2.py


class Demo:
    def load(self, rule):
        parse = None
        # 根据不同的rule，创建不同的对象
        if "xml" == rule:
            parse = XmlParse()
        elif "json" == rule:
            parse = JsonParse()
        elif "json" == rule:
            parse = ExcelParse()
        elif "json" == rule:
            parse = CsvParse()
        else:
            parse = OtherParse()
        # 调用对象的方法进行操作
        parse.parse()


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