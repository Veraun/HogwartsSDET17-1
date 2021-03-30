#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/30 21:04
# @Author  : Warren.wang
# @File    : send_rocketMq.py
# @Software: PyCharm

from rocketmq.client import Producer, Message

product = Producer("PID-123")
product.set_namesrv_addr("ip:port")
product.start()

msg = Message("主题")
msg.set_keys("keys")
msg.set_tags("标签")
msg.set_body("发送的数据")
ret = product.send_sync(msg)
print(ret.status, ret.msg_id, ret.offset)

