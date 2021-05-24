'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: demo.py
@time: 2021/5/21 10:52
@Email: Warron.Wang
'''

from flask import Flask, request

# 初始化Flask实例
# Flask是一个wsgi应用 (WSGI是一套协议，使WEB应用和服务器交互)
# __name__给Flask一个名称
app = Flask(__name__)

# 定义路由，当访问路由中定义的url时，就会执行下面的函数
# / 代表根，也就是说当浏览器什么都不输入的时候就会访问根
@app.route("/")
def hello_world():
    # Flask函数的返回值，默认是html类型
    # 如果返回是字典，就是json类型
    return "<p>Hello,World!</p>"

# methods 可以指定监听请求类型，可以是GET/POST...(默认是GET)
@app.route("/hello", methods=['GET', 'POST'])
def hello():
    return "<p>Fine Thank You!</p>"

# 可以通过 http://127.0.0.1:5000/param?a=b&c=k
@app.route("/param", methods=["POST", "GET"])
def get_param():
    # 可以利用request.args获取两个参数
    # 为什么 request.args可以获取两个参数？？？
    # return request.args

    # 可以利用 request.json获取post传过来的请求体
    return request.json

# Flask中<>代表变量，会把真实url中的<abc>中的内容传递给对应变量
@app.route("/param/<abc>", methods=["POST", "GET"])
def get_var(abc):
    return abc

if __name__ == '__main__':
    # 运行服务 Flask默认监听 127.0.0.1：5000 ,只要发送get或其他请求，就会触发路由
    # debug 参数：启动调试模式(当代码发生变化时，Flask会自动运行)
    app.run(debug=True)