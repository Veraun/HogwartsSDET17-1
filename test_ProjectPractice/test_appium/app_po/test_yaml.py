'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: test_yaml.py
@time: 2021/3/9 23:26
@Email: Warron.Wang
'''

# python 自带的日志收集模块
import logging

import yaml

logging.basicConfig(level=logging.INFO)


def test_yaml():
    logging.info("test_yaml")

    pythonobj = {
        'desirecaps': {'platformName': 'android', 'deviceName': 'emulator-5554', 'appPackage': 'com.tencent.wework',
                       'appActivity': '.launch.LaunchSplashActivity', 'noReset': 'true',
                       'skipServerInstallation': 'true',
                       'skipDeviceInitialization': 'true'}, 'server': {'ip': '127.0.0.1', 'port': 4723}}
    print(yaml.safe_dump(pythonobj))
    print(yaml.safe_dump(pythonobj))
    logging.info(yaml.safe_dump(pythonobj))