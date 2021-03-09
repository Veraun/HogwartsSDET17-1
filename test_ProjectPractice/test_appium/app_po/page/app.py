'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-
@author: wangwei
@project: HogwartsSDET17
@file: app.py
@time: 2021/3/7 16:02
@Email: Warron.Wang
'''

# 启动app、停止app、重启app
import yaml
from appium import webdriver

from test_ProjectPractice.test_appium.app_po.page.base_page import BasePage
from test_ProjectPractice.test_appium.app_po.page.main_page import MainPage


with open("../datas/caps.yml") as f:
    datas = yaml.safe_load(f)
    desires = datas['desirecaps']
    ip = datas['server']['ip']
    port = datas['server']['port']

class App(BasePage):
    def start(self):
        # # 启动app
        # caps = {}
        # caps["platformName"] = "android"
        # caps["deviceName"] = "emulator-5554"
        # caps["appPackage"] = "com.tencent.wework"
        # caps["appActivity"] = ".launch.LaunchSplashActivity"
        # caps["noReset"] = "true"
        # # 跳过安装uiautomator2server等 服务
        # caps['skipServerInstallation'] = "true"
        # # 跳过设备的初始化
        # caps['skipDeviceInitialization'] = "true"
        # # 运行前不停止app
        # # caps['dontStopAppOnReset'] = "true"
        #
        # # caps['settings[waitForIdleTimeout]'] = 1
        # # 客户端与appium 服务器建立连接的代码
        # self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        # self.driver.implicitly_wait(5)
        # return self
        if self.driver == None:
            # 启动app
            # 客户端与appium 服务器建立连接的代码
            self.driver = webdriver.Remote(f"http://{ip}:{port}/wd/hub", desires)
            self.driver.implicitly_wait(5)
        else:
            # self.driver.start_activity("com.tencent.wework",".launch.LaunchSplashActivity")
            self.driver.launch_app()
        return self

    def restart(self):
        # 停止app
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        # 重启app
        self.driver.quit()

    def goto_main(self):
        # 进到首页
        return MainPage(self.driver)
