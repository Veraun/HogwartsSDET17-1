## 第一部分---pytest实战
霍格沃兹测开17期实战演练---计算器

## 霍格沃兹论坛
- [测试人论坛](https://ceshiren.com/)

## 目的
- Pytest框架实战
- 计算器功能实战

## 参考链接
pytest：https://docs.pytest.org/en/stable/getting-started.html

## 西西老师课堂资源
- https://ceshiren.com/t/topic/9879
- https://ceshiren.com/t/topic/9936

## 个人作业地址
- https://github.com/wiki918/HogwartsSDET17.git

## 项目框架结构
- Testcases：主要测试用例文件夹 
  - test_calculatorNew.py：主要测试用例
    - 使用fixture进行参数化
    - 引入allure测试组件添加到测试用例中，使其在报告中更具可读性 
  - conftest.py：包括get_data代码，使用pytest可以自动激活
  - report.log：由编写的logger自定义的fixture生成
  - reports/allure_results：使用pytest.ini设置自动生成
    - 与检查 allure serve reports/allure_results
  - datas：使用yaml格式测试数据，让测试用例管理更人性化
- pythoncode：被测方法目录
  - Calculator.py：计算器功能
- pytest-encode：有关编码和日志的自定义fixture
  - 使用以下命令安装此插件：
    - pip install dist/pytest_encode-1.0-py3-none-any.whl
  - 安装后，您可以使用日志和中文用例显示功能
- requirement.txt：插件和依赖项，它们需要安装在您的虚拟环境中
    - 安装：pip install -r requirement.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
    - 导出：pip freeze > requirements.txt
- pytest.ini：一些有用的命令行，包括addopts设置和诱人的报告生成，它们会在程序启动时自动激活

## 使用Allure报告
- 1. 安装 allure2
- 2. Allure help  帮助文档 
- 3. 生成 allure 测试结果 ：切到用例执行文件下，如testing文件下。
  - pytest —alluredir=./report/allure_results
- 4. 展示报告：allure serve ./report/allure_results
- 5. 生成最终版本的报告：   allure generate ./report/allure_results
- 6. 在本地搭建一个网站服务（例如：Django）
  - python manage.py runserver  (http://127.0.0.1:8000/)
  

************************************************
************************************************


## 第二部分---selenium实战
selenium实战联演

## 项目框架结构
- selenium_demo：测试demo
- selenium_event:各种事件
- selenium_frame_window:多窗口、frame
- selenium_file_alert:文件上传、alert弹窗
- selenium_js:js操作

## 复用已有浏览器
- 参考帖子
    - https://ceshiren.com/t/topic/3567
- 浏览器
    - chrome -remote -debugging -port = 9222
- python
    - chrome_arg = webdriver.ChromeOptions()
    - chrome_arg.debugger_address = '127.0.0.1:9222'
    - self.driver = webdriver.Chrome()
- 环境设置及启动命令
    - Windows/Linux命令为：chrome --remote-debugging-port=9222 (9222为端口号，可以换成任意一个没有被占用的端口)
    - Mac命令为：Google\ Chrome --remote-debugging-port=9222 (9222为端口号，可以换成任意一个没有被占用的端口) (注意命令中间的反斜线)


************************************************
************************************************ 
 
## 第三部分---appium实战：原生应用(Native App)

### 环境准备
- jdk 1.8版本
- Android sdk
- Nodejs(>=10版本)、npm(>=6版本)
- python3
- appium-desktop
- Appium python client
- windows + 是夜神/木木这类模拟器 是需要手动adb connect一下
- mac + 是夜神/木木这类模拟器 ,只需adb kill-server，然后再adb devices

### 常用命令
#### app信息
- 获取当前界面元素:adb shell dumpsys activity top（推荐）（重点）
- 获取任务列表:adb shell dumpsys activity activities
#### app入口
- 获取appPackage和appActivity：
    - adb logcat | grep -i displayed （推荐）（重点）
    - Mac/Linux：adb logcat |grep -i activitymanager
    - Windows：adb logcat |findstr /i activitymanager
    - 如：02-18 16:07:42.819   479   690 I ActivityManager: Displayed com.xueqiu.android/.view.WelcomeActivityAlias: +5s97ms
- 在模拟器当前页面，获取appPackage和appActivity ： adb shell dumpsys window | grep mCurrent
- aapt dump badging mobike.apk | grep launchable-activity
- apkanalyzer最新版本的sdk中才有
#### 启动应用
adb shell am start -W -n com.xueqiu.android/.view.WelcomeActivityAlias -S （重点）

### 三种经典等待方式
#### 强制等待 
- sleep 不推荐
#### 隐式等待
- (全局性)生效
- 设置一个超时时间，服务端appium会在给定的时间内，不停地查找，默认值是0
- 用法：driver.implicitly_wait(10, TimeUnit.SECONDS)
- 在服务端等待
- 默认尽量加上，限定在3-6秒，为了所有的find_element方法都有一个很好的缓冲
- 只有查找页面元素，才会触发隐式等待
#### 显示等待(等待某个元素)
- (局部)生效
- Element = WebDriverWait(driver,10,0.5).until(expected_conditions.visibility_of_element_located((MobileBy.ID,"com.android.settings:id/title")))
- 在客户端等待
- 用来处理隐式等待无法解决的一些问题。如：文件上传
- 显示等待可以设置的长一点
### 定位方法
#### 测试步骤三要素
- 定位、交互、断言
#### 测试步骤三要素
- id定位
- accessibility_id定位
- xpath定位
- classname定位(不推荐)
### 定位工具
#### uiautomatorviewer工具(only android)
- 推荐使用
- sdk路径下的工具
#### Appium inspector工具

### 高阶定位方法
- uiautomator
  - self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("wiki")

- 滚动查找指定元素
  - self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("轻金融").'
                                                        'instance(0));').click()

### toast定位
- appium使用uiautomator底层的机制来分析抓取toast，并且把toast放到控件树里，但本身并不属于控件
- automatorName：uiautomator2
- 必须使用xpath查找
  - //*[@class='android.widget.Toast']
  - //*[contains(@text, 'popup menu item Search')]
  
### 属性获取
- print(search_ele.get_attribute("content-desc"))
- print(search_ele.get_attribute("resource-id"))
- print(search_ele.get_attribute("enabled"))
- print(search_ele.get_attribute("clickable"))
- print(search_ele.get_attribute("bounds"))

### 断言
- 普通断言
  - assert
- Hamcrest断言
  - github地址：https://github.com/hamcrest/PyHamcrest
  - hamcrest框架是一个为了测试为目的，能组合成灵活表达式的匹配器类库。
  - 提供了大量被称为"匹配器"的方法。每个匹配器都设计用于执行特定的比较操作
  - 支持多种语言。如java、python等
  
  
### 参数化用例
`@pytest.mark.parametrize("search_key, type, expect_price",[
        ('alibaba', 'BABA', 250),
        ('xiaomi', '01810', 28)
    ])`


************************************************
************************************************ 
 
## 第四部分---appium实战：网页端应用(webview App,浏览器可以打开的应用)
### 环境准备
- 手机端
  - 被测浏览器：safari、Chrome、browser(不可以是第三方浏览器)
  - 查看模拟器里安装的所有应用包：adb shell pm list package
  - 查看模拟器里安装的浏览器应用包：adb shell pm list package | grep browser
  - 查看模拟器里安装的浏览器应用版本号：adb shell pm dump com.android.browser | grep version
  

- PC端
  - 下载对应手机浏览器的driver版本：
    - https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md
    - https://chromedriver.storage.googleapis.com/index.html?path=2.20

- 客户端代码
  - ``
des_caps = {
            "platformName": "android",
            "platformVersion": "6.0.1",
            "browserName": "Browser",  # 被测浏览器
            "deviceName": "emulator-5554",
            "noReset": True,  # 去掉页面弹窗
            "chromedriverExecutable": "/Users/xmly/Documents/chromedriver20"  #Chromedriver地址
        }
``

- Chromedriver地址
  - 将下载好的webdirver放在下面任一路径下
  - 1默认地址：appium自动读取，
    - /Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac
  - 2可自定义路径
    - /Users/xmly/Documents/chromedriver20

### 元素定位
#### 前提条件
  - 1.浏览器能访问https://www.google.com
  - 2.下载对应手机浏览器的driver版本：                                                           
    - https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/
    - https://chromedriver.storage.googleapis.com/index.html?path=2.20 
- 方式一：
    - 1只能通过PC上的Chrome浏览器，输入：chrome://inspect/#devices
    - 2点击页面上的inspect，弹出页面，进行元素定位
- 方式二：
    - 下载UC浏览器开发者版本
        - webview调试工具(无需科学上网)
        - http://192.168.60.25:7788/panda/index#/taskDependent




************************************************
************************************************ 
 
## 第五部分---appium实战：混合应用(Hybrid App)

### 如何判断app里有页面是webview
- 1.断网查看
- 2.看加载条
- 3.看顶部是有有关闭按钮
- 4.下拉刷新，页面是否刷新
- 5.下拉刷新的时候，是否有网页提供方
- 6.用工具查看：里面有webview的字眼

### 前提条件
- PC：
  - 1.浏览器能访问https://www.google.com
  - 2.下载对应手机浏览器的driver版本：                                                           
    - https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/
    - https://chromedriver.storage.googleapis.com/index.html?path=2.20            

- 手机端：
  - 应用代码需要打开webview开关

- 代码：
  - appPackage，appActivity
  - desirecapability里添加：chromedriverExecutable ：driver路径

- 模拟器安装：支持android6.0
    - 安装文档：https://blog.csdn.net/zww1984774346/article/details/51888218
    - 软件名：Genymotion 登录名：wangwei806881231@163.com  https://www.genymotion.com/download/
    - 软件名：VirtualBox  https://www.virtualbox.org/wiki/Downloads

### appium实战遇到的坑
- 设备
    - android模拟器6.0默认支持webview操作
    - Genymotion和sdk自带的emulator可以
    - 其他物理机和其他模拟器(如：mumu模拟器)不可以，需要开发人员打开app内开关(webview调试开关)
- PC浏览器定位元素
    - chrome浏览器-Chrome62才可以更好的看见webview内部，其他版本可能有bug
    - 也可换成chromium浏览器可以避免很多坑，展示效果和速度比chrome要快
- 代码
    - 有的设备可以直接使用find_element_by_accessibility_id(),不同设备渲染的页面不同，兼容性不适合
    - 使用switch_to.context()
    - 使用switch_to.window()
    
### appium的capability使用进阶
 - 参考文档：http://appium.io/docs/en/writing-running-appium/caps/#android-only
 - 普通：
     - newCommandTimeout: 找下一个元素的等待时间
     - udid: 满足多设备时的唯一标识
     - autoGrantPermissions: 授予各类弹框权限，自动把弹框点掉
        - 当noReset=True时，此项不生效
 - 测试策略：
     - noReset ：不停止应用程序，不清除应用程序数据，也不卸载APK
     - fullReset：停止应用程序，清除应用程序数据，卸载APK
     - dontStopAppOnReset：不会kill应用，会继续执行后续用例
       - 相当于adb shell am start com.tencent.wework/com.tencent.wework.launch.LaunchSplashActivity
 - 性能相关：启动时设置
     - skipServerInstallation：跳过安装uiautomator2server等 服务
     - skipDeviceInitialization：跳过设备的初始化
     - skipUnlock
     - skipLogcatCapture
     - systemPort
     - ignoreUnimportantViews
     - relaxed-security
 - 辅助定位工具
   - weditor：https://www.cnblogs.com/RuguoCheng/p/10457637.html

### 微信小程序测试
 
 
 
************************************************
************************************************ 
    
## 第六部分---实战项目

### appium-企业微信app项目实战1

标题
app 企业微信实战（一）

课程价值
了解 Appium 框架结构
掌握 Appium 环境搭建
掌握 Appium Inspector 录制及查找元素的使用
掌握 DesireCapability 用法

大纲
Appium 介绍
Appium 环境搭建
Appium Inspector
企业微信实战-自动打卡


PPT
课堂 ppt https://pdf.ceshiren.com/ck17/appium1 PPT地址
参考链接
SDK安装：Android Studio安装(推荐使用这种方法安装SDK) 6
appium 官网： appium.io 1
appium 环境搭建：

Android 环境配置：Appium 环境搭建（ windows 版本 | Mac版本） 5
iOS 环境配置：IOS自动化配置 2
mumu 模拟器：https://mumu.163.com/help/

脚本编写
应用
Appium 框架结构

appium 工作引擎

- 如何选择一款合适的测试设备
    - 真机
        - 打开 开发者选项(设置-关于-找到【版本号】连点七下-返回上一层 - 打开usb调试模式)
        - 安装手机驱动（ 手机助手 或者 豌豆夹…）
        - 执行adb devices
    - 模拟器
        - mumu模拟器，夜神，逍遥，genimotion，emulator

- mumu 模拟器的连接方式
    - 【win版】
        - adb connect 127.0.0.1:7555
        - adb shell

    - 【mac版】

        - adb kill-server && adb server && adb shell
`


安装应用
将下载好的apk拖到手机里
使用 adb install 命令安装
adb install -r  /path/to/com.tencent.wework_3.1.2_14198.apk 


android 日志
adb logcat '*:E' 收集Error 及Error 以上级别 的日志 

mac/Linux： adb logcat ActivityManager:I | grep "cmp"
Windows:adb logcat ActivityManager:I | findstr "cmp"
企业微信企业页名：com.tencent.wework/.launch.LaunchSplashActivity（包名/启动页名）

验证是否能够启动成功
adb shell am start -n com.tencent.wework/.launch.LaunchSplashActivity

DesireCapability
settings 控制 动态页面的等待时长

参考代码
class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps['settings[waitForIdleTimeout]'] = 1
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        '''
        前提条件: 已登录状态（ noReset=True）
        打卡用例：
        1、打开【企业微信】应用
        2、进入【工作台】
        3、点击【打卡】
        4、选择【外出打卡】tab
        5、点击【第N次打卡】
        6、验证【外出打卡成功】
        7、退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH, "//android.view.ViewGroup//*[@text='工作台']").click()
        # android_uiautomator 里面要用双引号，外面用单引号。
        # 向下滑动两次，再向上查找，直到找到元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        print(self.driver.page_source)
        # sleep(2)
        # assert "外出打卡成功" in self.driver.page_source
        # 激活隐式等待
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")


作业
思考题：

1如何封装滑动查找？（swipe TouchAction）
    - https://github.com/wiki918/HogwartsSDET17/blob/main/test_ProjectPractice/test_appium/test_wework.py
2完成企业添加联系人
    - https://github.com/wiki918/HogwartsSDET17/blob/main/test_ProjectPractice/test_appium/test_swipe_find.py


### appium-企业微信app项目实战2

- 课程价值
    - 掌握 元素定位几种方式
    - 掌握 元素定位技巧
    - 掌握 PO 设计模式
- 大纲
    - 元素定位的几种常用方式
    - 元素定位技巧
    - 特殊控件Toast获取
    - 引入 PageObject 设计模式

- PPT
 - 课堂ppt https://pdf.ceshiren.com/ck17/appium2 PPT地址

- 应用
 - 参考链接
   - flutter ： https://github.com/truongsinh/appium-flutter-driver 

- DesireCapability 设置
    - appium:skipServerInstallation 跳过UIautomator2 server安装
    - skipDeviceInitialization  跳过设备的初始化
    - dontStopAppOnReset   测试之前不停止app运行

测试步骤三要素
* 定位、交互、断言

定位方式
* **Id** **定位（优先级最高）**
* **XPath** **定位（速度慢，定位灵活）**
* **Accessibility ID** **定位（****content-desc****）**
* Uiautomator 定位（速度快，语法复杂）

XPATH 定位方式
* 全称：XML PATH

xpath 官网：https://www.w3.org/TR/2017/REC-xpath-31-20170321/ 

xpath function 的用法：https://www.w3.org/TR/xpath-functions/#func-starts-with 

绝对定位: 不推荐
相对定位：
//*
//*[contains(@resource-id, ‘login’)]（重点）
//*[@text=‘登录’] （重点）
//*[contains(@resource-id, ‘login’) and contains(@text, ‘登录’)] （重点）
//*[contains(@text, ‘登录’) or contains(@class, ‘EditText’)]（了解）
//[ends-with(@text,‘号’) ] | //[starts-with(@text,‘姓名’) ] 两个定位的集合列表**（了解）**
//*[@clickable=“true"]//android.widget.TextView[string-length(@text)>0 and string-length(@text)<20]（了解）
//[contains(@text, ‘看点’)]/ancestor:://*[contains(@class, ‘EditText’)] （轴）（了解）

原生定位器
* 官网
https://developer.android.com/reference/android/support/test/uiautomator/UiSelector.html 
Uiautomator 定位
* 写法：’new UiSelector().text(“text")’
* 滚动查找：
  - new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(“查找的文本”).instance(0));


- PO 封装
* 1、app.py 封装起来(应用的启动，关闭，重启)
* 2、将各个页面以Page页的形式封装起来
* 3、driver 复用，封装base_page.py 将__init__方法，find(),finds(), swipe_find() 底层常用的一些方法封装起来，driver 不要暴露出来。

- PO模式封装的主要组成元素
  - Page对象：完成对页面的封装
  - driver对象：完成对web、android、ios、接口的封装
  - 测试用例：调用Page对象实现业务业务并断言
  - 数据封装：配置文件和数据驱动
  - Utils：其他功能的封装，改进原生框架的不足
  
日志 收集
设置日志级别

logging.basicConfig(level=logging.INFO)

打印日志

logging.info("find")
logging.info(locator,value)
logging 日志级别划分

_nameToLevel = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET,
python 会收集当前级别及以上级别的日志。

参考代码

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from time import sleep

from selenium.common.exceptions import NoSuchElementException


class TestContact:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        # 跳过安装uiautomator2server等 服务
        caps['skipServerInstallation'] = "true"
        # 跳过设备的初始化
        caps['skipDeviceInitialization'] = "true"
        # 运行前不停止app
        # caps['dontStopAppOnReset'] = "true"

        # caps['settings[waitForIdleTimeout]'] = 1
        # 客户端与appium 服务器建立连接的代码
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def swipe_find(self, text, num=3):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找到{num}次， 未找到。")

            self.driver.implicitly_wait(1)
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(5)
                return element
            except:
                print("未找到")
                size = self.driver.get_window_size()
                width = size.get('width')
                height = size.get("height")

                start_x = width / 2
                start_y = height * 0.8

                end_x = start_x
                end_y = height * 0.3

                self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def test_addcontact(self):
        name = "hogwarts_2"
        phonenum = "13100000002"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        element = self.swipe_find("添加成员")
        element.click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='必填']").send_keys(phonenum)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        # 验证添加成员 toast
        # sleep(1)
        # print(self.driver.page_source)
        # assert '添加成功' in self.driver.page_source
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成功']")


课后作业
思考题：
1.如何将日志保存到文件中？

课后练习：

实现添加联系人功能的PO封装
实现删除联系人功能的PO封装
https://github.com/wiki918/HogwartsSDET17/blob/main/test_ProjectPractice/test_appium/app_po/testcases/test_contact.py
 
************************************************
************************************************ 

## 第七部分---ui自动化测试框架

### 设备交互API
        # 测试过程中模拟来电
        self.driver.make_gsm_call('13524630000', GsmCallActions.CALL)
        # 测试过程中模拟来短信
        self.driver.send_sms('13524630000', 'hello appium api')
        # 测试过程中模拟切换网络
        self.driver.set_network_connection(1)
        # 测试过程中截图
        self.driver.get_screenshot_as_file('./photos/img.png')
        # 测试过程中模拟开始视频录制
        self.driver.start_recording_screen()
        # 测试过程中模拟结束视频录制
        self.driver.stop_recording_screen()
        


************************************************
************************************************ 

## 第八部分---打造自己的ui自动化测试框架
### 标题
 -打造自己的测试框架 （一）

### 课程价值
    - UI自动化测试框架目标
    - 使用雪球app复用框架
    - 黑名单机制
### 框架的价值
    - 把业务代码的重复性功能，放入框架
    - 把框架移植到新的业务
    - UI自动化测试框架：
        易用
        基础的功能封装（appium代码）
        完成弹窗处理
        截图
        录屏
        日志
### 雪球 app
    包名： com.xueqiu.android
    活动名：.view.WelcomeActivityAlias
    
### 作业
 - 提取基础框架，用框架实现雪球的点击行情

 - 将黑名单功能放到装饰器，装饰 find 方法 （提高）
 
 
### 标题
 - 打造自己的测试框架 （二）

### 课程价值
    UI自动化测试框架优化
    使用关键字驱动
    使用录屏:scrcpy
      mac安装：brew install scrcpy
      命令执行：scrcpy -p 1234 -m 800 -Nr tmp.mp4
      文档：https://github.com/Genymobile/scrcpy/issues/382
    使用截屏
    使用log
    使用allure
        pytest test_market.py --alluredir=./result
        allure serve ./result 


### 使用装饰器改造黑名单 
 - 意义
 - 实现
 
        # 装饰器使用
        def b(func): #func == a
            def run(*args, **kwargs):  # args == ("我是k")
                print("你好")
                func(*args, **kwargs)  # 装饰器：调用a("我是k")
                print("再见")
            return run
        
        @b
        def a(k):       # 被装饰对象
            print("我是a")
            print(k)
        
        def test():     # 调用
            a("我是k")
 
 
 - 将黑名单功能移动到装饰器

        def black_wrapper(fun):
    
            def run(*args, **kwargs):
        
                basepage = args[0]
        
                try:
        
                    return fun(*args, **kwargs)
        
                # 捕获元素没找到异常
        
                except Exception as e:
        
                    # 遍历黑名单中的元素，进行处理
        
                    for black in basepage.black_list:
        
                        eles = basepage.finds(*black)
        
                        # 黑名单被找到
        
                        if len(eles) > 0:
        
                            # 对黑名单元素进行点击，可以自由扩展
        
                            eles[0].click()
        
                            return fun(*args, **kwargs)
        
                    raise e
        
            return run

### 关键字驱动
 - 意义

 - 实现
    - 使用 pyyaml 加载 yaml 文件
    
    - 使用分支实现不同关键字
    
    - 将企业微信的 PO 改造成关键字驱动


        goto_market:
        
          - by: xpath
        
            locator: "//*[@resource-id='android:id/tabs']//*[@text='行情']"
        
            action: click


        def load(self, yaml_path):
    
            with open(yaml_path, encoding="utf-8") as f:
    
                data = yaml.load(f)
    
            for step in data:
    
                xpath_expr = step.get(self.FIND)
    
                action = step.get(self.ACTION)
    
                if action == self.FIND_AND_CLICK:
    
                    self.find_and_click(By.XPATH, xpath_expr)
    
                elif action == self.SEND:
    
                    content = step.get(self.CONTENT)
    
                    self.send(By.XPATH, xpath_expr, content)

### 录屏 
 - 意义

 - 实现
    - 介绍 scrcpy 使用：原理，录屏
    
    - 使用 subprocess 操作 scrcpy 进行录屏

            import os
            
            import signal
            
            import subprocess
            
            import pytest
            
            @pytest.fixture(scope='module', autouse=True)
            
            def record_vedio():
            
                cmd = "scrcpy --record file.mp4"
            
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            
                print(p)
            
                yield
            
                os.kill(p.pid, signal.CTRL_C_EVENT)

### 截图
 - 意义
 - 实现
    - 使用 Appium 进行截图
    
    - 使用 allure 加载


    # 放入 allure 报告
    allure.attach(self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

### log定制
 - 意义
 - 实现
    - 原理：两部曲
     - 1、log_init()
     - 2、log.debug("新定位元素是：%s", args[2])
    - 代码



        # 定义 log 的基础内容
        
        def log_init():
        
            # 设置格式
        
            log_format_str = '[%(asctime)s]  %(filename)s:%(lineno)d:%(funcName)s: %(message)s'
        
            format = logging.Formatter(log_format_str)
        
            # 根据 log 标识获取 log
        
            root = logging.getLogger("my_log")
        
            # 加入文件句柄
        
            h = logging.handlers.RotatingFileHandler("./tmp.log", mode='a', encoding="utf-8")
        
            h.setFormatter(format)
        
            # 加入输出流句柄
        
            s = logging.StreamHandler()
        
            s.setFormatter(format)
        
            root.addHandler(h)
        
            root.addHandler(s)
        
            root.setLevel(logging.DEBUG)
        
        # 获取 log
        
        log = logging.getLogger("my_log")


************************************************
************************************************ 

## 第九部分---客户端测试平台

### 自动遍历测试技术
    Google android原生的monkey、app crawler
    百度smartmonkey
    腾讯newmonkey
    vigossjjj smart_monkey
    macaca的NoSmoke
    头条的zhangzhao maxim
    seveniruby appcrawler （重点讲这个）

### android monkey健壮性测试工具
 - adb shell monkey 100 对所有包随机操作
 - adb shell monkey -p com.xueqiu.android 100 对指定包 
 - adb shell monkey -p com.xueqiu.android -s 20 80 时间种子 
 - adb shell monkey -p com.xueqiu.android -vv -s 20 80 详细日志
 - adb shell monkey -p com.xueqiu.android --throttle 5000 100 时间延迟
 - adb shell monkey -p com.xueqiu.android --pct-touch 10 1000 事件百分比
 - 综合场景：adb shell monkey -p com.xueqiu.android -vv --throttle 500 --pct-touch 90 200
 
 - 常用事件
   --pct-touch：触摸事件，比如点击
   --pct-motion：动作事件，比如滑动（直线）
   --pct-trackball：轨迹事件，比如移动+点击，曲线滑动
   --pct-majornav：主要导航事件，比如回退按键、菜单按键
   
### android maxim 遍历测试工具
 - github：https://github.com/zhangzhao4444/Maxim.git
 - push两个文件到手机的sdcard
  - adb push framework.jar /sdcard
  - adb push monkey.jar /sdcard
 - git文档技术支持
  - https://github.com/zhangzhao4444/Maxim
  - cmd 固定命令 ： 
   - adb shell CLASSPATH=/sdcard/monkey.jar:/sdcard/framework.jar exec app_process /system/bin tv.panda.test.monkey.Monkey -p com.xueqiu.android --uiautomatormix --running-minutes 60 -v -v
        tv.panda.test.monkey.Monkey： monkey入口类，不要修改
        com.xueqiu.android： 被测app包名，需要修改
        --uiautomatormix： 遍历策略
        
### 多平台自动化遍历测试工具：appcrawler （思寒大佬，推荐）
#### 开源地址
 - https://github.com/seveniruby/AppCrawler
#### appcrawler底层依赖
 - appium
 - adb
 - macaca
 - selenium
#### appium底层引擎
 - wda
 - uiautomator2AppCra


### 跨平台设备管理方案-selenium grid
#### 优点
 - 所有测试的中心入口点
 - 管理和控制浏览器运行的Node/环境
 - 扩展
 - 并行运行测试
 - 跨平台测试
 - 负载平衡
#### 下载
 - https://www.selenium.dev/downloads/
#### 配置NodeWebDriver.json
 - https://github.com/SeleniumHQ/selenium/blob/selenium-3.141.59/java/server/src/org/openqa/grid/common/defaults/DefaultNodeWebDriver.json
#### 启动执行
 - 1进入jar文件下载路径，启动主机：java -jar selenium-server-standalone-3.141.59.jar -role hub
 - 2进入jar文件下载路径，启动子机1：java -jar selenium-server-standalone-3.141.59.jar -role node -nodeConfig node.json
 - 3进入jar文件下载路径，启动子机2：java -jar selenium-server-standalone-3.141.59.jar -role node -nodeConfig node.json
#### 目的
 - 脚本运行对node进行分发
#### 脚本
 - selenium_grid/test_grid.py