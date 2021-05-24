'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_client.py
@time: 2021/5/14 10:36
@Email: Warron.Wang
'''

import pymysql

db = pymysql.connect(
    host='192.168.60.11',
    user='naliworld',
    password='password!',
    db='XIMA_BF_ACC',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def test_conn():
    with db.cursor() as cursor:
        sql = "show tables;"
        cursor.execute(sql)
        print(sql)
        print(cursor.fetchall())

def test_select():
    with db.cursor() as c:
        sql = "SELECT * FROM ACC_ACCOUNT where user_id = %s ORDER BY CREATE_TIME DESC;"
        c.execute(sql, ["1155780"])
        print(c.fetchall())