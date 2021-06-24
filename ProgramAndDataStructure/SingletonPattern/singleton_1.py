'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: singleton_1.py
@time: 2021/6/5 17:31
@Email: Warron.Wang
'''

'''
饿汉式单例：类加载时就会创建实例

利：避免运行中卡顿，在初始化阶段就能发现错误
弊：提前初始化浪费资源
'''

class IdMaker:
    # python的类变量：会被多个类、实例共享
    __instance = None
    # id 也是类变量：会被多个类、实例共享
    __id = -1
    # python 在类加载阶段，通过父类的 __new__创建实例
    # 如果我们重写 __new__ 就不会调用父类的 __new__，就会调用我们自己重写的 __new__创建的实例
    # __new__需要返回一个实例，如果不返回就不会实例化

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # 父类的__new__，参数接收一个类名，会返回类的实例
            cls.__instance = super().__new__(cls)
        return cls.__instance

    # 计数器，在获取前，进行 +1
    def get_id(self):
        self.__id += 1
        return self.__id


def test_id_maker():
    # IdMaker 是单例类，只允许有一个实例
    id1 = IdMaker().get_id()
    id2 = IdMaker().get_id()
    id3 = IdMaker().get_id()
    print(id1, id2, id3)

if __name__ == '__main__':
    test_id_maker()