'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: workdirly
@file: jenkins_requests.py
@time: 2021/4/20 19:05
@Email: Warron.Wang
'''
import json

import requests

# url = "http://admin:123456@192.168.96.223:8086/job/warron_firstjob/build"
# ret = requests.post(url)
# print(ret.text)


# url = "http://admin:123456@192.168.96.223:8086/job/warron_firstjob/lastBuild/buildNumber"
# ret = requests.get(url)
# print(ret.text)


url = "http://admin:123456@192.168.96.223:8086/job/warron_firstjob/2/api/json"
ret = requests.get(url)
print(json.dumps(ret.json(), indent=2))