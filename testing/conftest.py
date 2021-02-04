#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/31 17:07
# @Author  : Warren.wang
# @File    : conftest.py
# @Software: PyCharm

'''
要点1：文件名时固定的，不能改
要点2：执行测试用例之前，先去执行conftest文件
'''

import datetime
from typing import List
import pytest
import yaml

@pytest.fixture(scope='session', autouse=True)
def conn_db():
    print("完成 数据库连接")
    yield "database"
    print("关闭 数据库连接")

@pytest.fixture(scope="function", params=['tom', 'jerry'])
def login(request):
    # setup 操作
    print("登录操作")
    username = request.param
    # yield 相当于return 操作
    yield username
    # teardown操作
    print("登出操作")

#命令行
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts-Warron")  # 下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 默认值
                      dest='env',  # 存储的变量
                      help='set your run env'  # 参数说明
                      )

@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')

    if myenv == 'test':
        datapath = "datas/test/data.yml"
    elif myenv == 'dev':
        datapath = "datas/dev/data.yml"

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    print(datas)

    return myenv, datas


#内置插件，只是重写方法  （hook函数）
#解决打印用例编码问题
# def pytest_collection_modifyitems(
#     session: "Session", config: "Config", items: List["Item"]
# ) -> None:
#     print(items)
#     for item in items:
#         '''
#         u = '中文' #指定字符串类型对象u
#         str = u.encode('gb2312') #以gb2312编码对u进行编码，获得bytes类型对象str
#         u1 = str.decode('gb2312')#以gb2312编码对字符串str进行解码，获得字符串类型对象u1
#         u2 = str.decode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的字符串内容
#         '''
#         item.name = item.name.encode("utf-8").decode("unicode-escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")

    #     if "add" in item._nodeid:
    #         item.add_marker(pytest.mark.add)
    #
    # item.reverse()

def get_datas(name, type='int'):
    with open("./datas/calcNew.yml", encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']
    return (datas, ids)


#使用fixture进行参数化
@pytest.fixture(params=get_datas('add', 'int')[0], ids=get_datas('add', 'int')[1])
def get_datas_with_fixture(request):
    return request.param

@pytest.fixture(params=get_datas('add', 'int')[0], ids=get_datas('add', 'int')[1])
def get_add_int_datas_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas('add', 'float')[0], ids=get_datas('add', 'float')[1])
def get_add_float_datas_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas('div', 'int_normal')[0], ids=get_datas('div', 'int_normal')[1])
def get_div_int_normal_datas_with_fixture(request):
    return request.param


@pytest.fixture(params=get_datas('div', 'int_error')[0], ids=get_datas('div', 'int_error')[1])
def get_div_int_error_datas_with_fixture(request):
    return request.param