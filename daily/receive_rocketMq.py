#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 21:39
# @Author  : Warren.wang
# @File    : receive_rocketMq.py
# @Software: PyCharm

# 接受消息

import time
from rocketmq.client import PushConsumer, PullConsumer

def callback(msg):
    # 输出：主题、msg_id，接受的消息(进行utf-8转码)
    print(msg.topic, msg.id, (msg.body).decode("utf-8"))
    return PullConsumer

consumer = PushConsumer("CID_123") # 随便填
consumer.set_namesrv_addr("ip:port")
consumer.subscribe("主题", callback) # 发送消息时创建的主题
consumer.start()

while True:
    time.sleep(3600)
    consumer.shutdown()
