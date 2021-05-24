'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: flask_app.py
@time: 2021/5/13 17:41
@Email: Warron.Wang
'''

# save this as app.py
# 运行flask：env FLASK_APP=flask_app flask run
from flask import Flask, escape, request, session

app = Flask(__name__)
app.secret_key="warron"

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


# 发送post请求：curl -XPOST http://127.0.0.1:5000/login\?username\=warron\&password\=123456 -d "c=1"
@app.route("/login", methods=['post', 'get'])
def login():
    res = {
        "method": request.method,
        "url": request.url,
        "args": request.args,
        "form": request.form
    }
    session["username"] = request.args.get("name")

    return res  # 自动转json