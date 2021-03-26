'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: rewrite.py
@time: 2021/3/22 14:17
@Email: Warron.Wang
'''
import sys

from mitmproxy.tools.cmdline import mitmdump

"""
Basic skeleton of a mitmproxy addon.
Run as follows: mitmproxy -s anatomy.py
使用mitmproxy 实现rewrite功能：需要跟服务端进行交互
"""
import json

from mitmproxy import ctx, http


class Counter:

    def request(self, flow: http.HTTPFlow):
        pass
    def response(self, flow: http.HTTPFlow):
        # 判断请求的url 是否包含指定的url信息
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            # 拿到响应数据信息
            # flow.response.text 是str 属性，所以如果要是操作
            # 这个对象的话，必须转换为python 字典的数据结构
            # 否则就只能使用和str 相关的 方法
            data = json.loads(flow.response.text)
            data["data"]["items"][0]["quote"]["name"] = "warron很长很长的名称"
            # 反序列化回去
            flow.response.text = json.dumps(data)

# addons 是mitmproxy 的强制要求的规范
# 一定要使用此变量名存放类的实例
addons = [
    Counter()
]

# if __name__ == '__main__':
#     listen = 8080
#     sys.argv = [
#         __file__,
#         "-p", str(listen),
#         "-s", __file__
#     ]
#     mitmdump()