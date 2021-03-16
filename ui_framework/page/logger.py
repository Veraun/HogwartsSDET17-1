'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: logger.py
@time: 2021/3/16 09:32
@Email: Warron.Wang
'''


# 定义 log 的基础内容
import logging
import logging.handlers

def log_init():
    # 设置格式
    log_format_str = '[%(asctime)s]  %(filename)s:%(lineno)d:%(funcName)s: %(message)s'

    format = logging.Formatter(log_format_str)

    # 根据 log 标识获取 log
    root = logging.getLogger("app_log")

    # 加入文件句柄：把log写到文件中
    h = logging.handlers.RotatingFileHandler("./app.log", mode='a', encoding="utf-8")
    h.setFormatter(format)

    # 加入输出流句柄：把log输出到终端上
    s = logging.StreamHandler()
    s.setFormatter(format)

    # 加载句柄
    root.addHandler(h)
    root.addHandler(s)

    # 设置log等级
    root.setLevel(logging.DEBUG)


# 获取 log

log = logging.getLogger("app_log")