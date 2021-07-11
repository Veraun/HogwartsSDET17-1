## 专题：linux命令&bash脚本




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
- chrome驱动
    - https://chromedriver.storage.googleapis.com/index.html

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
- 小程序自动化测试关键步骤
    - 设置chromedriver正确版本
    - 设置chrome option传递给chromedriver
    - 使用adb proxy解决fix chromedriver的bug
    
- 微信小程序自动化测试辅助工具adb proxy

        使用代理技术解决了chromedriver和微信定制的chrome内核之间的调试问题，可以用于微信小程序的自动化测试。

- shell mock技术

        用于欺骗adb和appium，选择合适的chromedriver版本。个人使用可以先简单使用chromedriverExecutable代替

- 协议mock adb proxy实现
    - 运行命令

            mitmdump -p 5038 \
              --rawtcp --mode reverse:http://localhost:5037  \
              -s adb_proxy.py
  
- 辅助小程序测试的adb_proxy.py

        """
        测试人社区 https://ceshiren.com
        mitmdump -p 5038 --rawtcp --mode reverse:http://localhost:5037/ -s adb.py
        """
        from mitmproxy.utils import strutils
        from mitmproxy import ctx
        from mitmproxy import tcp
        
        
        def tcp_message(flow: tcp.TCPFlow):
            message = flow.messages[-1]
            old_content = message.content
            #message.content = old_content.replace(b"foo", b"bar")
            message.content = old_content.replace(b"@webview_devtools_remote_", b"@.*.*.*._devtools_remote_")
        
            ctx.log.info(
                "[tcp_message{}] from {} to {}:\n{}".format(
                    " (modified)" if message.content != old_content else "",
                    "client" if message.from_client else "server",
                    "server" if message.from_client else "client",
                    strutils.bytes_to_escaped_str(message.content))
            )

 
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
#### 昵称
 - app扫地机器人，爬虫
#### 开源地址
 - https://github.com/seveniruby/AppCrawler
#### appcrawler底层依赖
 - appium
 - adb
 - macaca
 - selenium
#### appium底层引擎
 - wda
 - uiautomator2AppCrawler
#### 环境依赖
 - java8
 - appium 1.8.x
#### 安装方式
 - 直接下载jar包
#### 启动
 - 启动appium
 - 启动模拟器或者真机
 - 开始自动遍历
#### 生成样板配置示例
 - java -jar appcrawler.jar --demo
   - 会在当前目录下生成一个demo.yml
 - 执行
   - 通过配置文件执行:java -jar appcrawler.jar -c demo.yml
#### 自动遍历支持
 - selectedList：需要被遍历的元素范围
 - firstList：优先被点击
 - lastList：最后被点击
 - tagLimitMax：同祖先(同类型)的元素最多点击多少次
 - backButton：当所有元素都被点击后默认后退控件定位
 - blackList：黑名单
 - maxDepth：6 遍历的最大深度(计算深度：根据activity)
#### 自动遍历过程(框架算法)
 - 信息获取
   - 把当前app的界面dump为xml结构
 - 获取待遍历元素
   - 遍历范围 selectedList
   - 过滤黑名单 小控件 不可见控件 blackList
   - 重排控件顺序 firstList lastList
   - 跳过已点击+跳过限制点击的控件 tagLimitMax
   - 根据匹配的规则执行action 
 - 循环上面的步骤



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
 
 
************************************************
************************************************ 

## 第十部分---服务端接口测试
### tcp协议分析
#### 抓包分析tcp协议
- 协议分析工具
    - 网络监听：TcpDump + WireShark
    - 代理Proxy
        - 推荐工具：手工测试charles[全平台]、全部测试burpsuite[全平台java]
        - 自动化测试：mitmproxy
        - 其他代理：fiddler[仅windows]、AnyProxy[全平台]
    - 协议客户端工具：curl、postman
#### TcpDump + WireShark配合使用
- 抓取访问百度的数据包
    - 1.sudo tcpdump host www.baidu.com -w /Users/xmly/Documents/wireshark/tmp/tcpdump.log
    - 2.curl http://www.baidu.com
    - 3.停止tcpdump
    - 4.使用wireshark打开tcpdump.log

#### TCP的三次握手与四次挥手
- 三次握手：在进行业务通信前，必须建立好连接
    - 第一次握手：建立连接时，客户端发送syn包（syn=j）到服务器，并进入SYN_SENT状态，等待服务器确认；SYN：同步序列编号（Synchronize Sequence Numbers）。
    - 第二次握手：服务器收到syn包，必须确认客户的SYN（ack=j+1），同时自己也发送一个SYN包（syn=k），即SYN+ACK包，此时服务器进入SYN_RECV状态；
    - 第三次握手：客户端收到服务器的SYN+ACK包，向服务器发送确认包ACK(ack=k+1），此包发送完毕，客户端和服务器进入ESTABLISHED（TCP连接成功）状态，完成三次握手。
- 四次挥手：选择关闭连接，以回收资源。“和平分手”
    - 第一次挥手：主动关闭方发送第一个包，其中FIN标志位为1，发送顺序号seq为X。
    - 第二次挥手：被动关闭方收到FIN包后发送第二个包，其中发送顺序号seq为Z，接收顺序号ack为X+1。
    - 第三次挥手：被动关闭方再发送第三个包，其中FIN标志位为1，发送顺序号seq为Y，接收顺序号ack为X。
    - 第四次挥手：主动关闭方发送第四个包，其中发送顺序号为X，接收顺序号为Y。至此，完成四次挥手。

### postman使用
- 创建接口测试集合
- 创建post(form、json、file)、get类型接口
- 设置和获取cookie、token
- 创建全局变量、插入断言
- 数据驱动(参数化)，支持csv、json文件
- 测试集的运行

### 使用curl发送请求
- 客户端模拟请求工具
    - nc tcp/udp协议发送
    - curl 最常使用的http请求工具
    - postman综合性的http协议测试工具
    - 代理工具、IDE工具、浏览器插件工具
    
- curl常见用法
    - url=http://www.baidu.com
    - get请求：curl $url
    - post请求：curl -d 'xxx' $url
    - proxy使用：curl -x 'http://127.0.0.1:8080' $url
- curl基本参数
        
        Usage: curl [options...] <url>
        Options: (H) means HTTP/HTTPS only, (F) means FTP only
             --anyauth       Pick "any" authentication method (H)
         -a, --append        Append to target file when uploading (F/SFTP)
             --basic         Use HTTP Basic Authentication (H)
             --cacert FILE   CA certificate to verify peer against (SSL)
             --capath DIR    CA directory to verify peer against (SSL)
         -E, --cert CERT[:PASSWD]  Client certificate file and password (SSL)
             --cert-status   Verify the status of the server certificate (SSL)
             --cert-type TYPE  Certificate file type (DER/PEM/ENG) (SSL)
             --ciphers LIST  SSL ciphers to use (SSL)
             --compressed    Request compressed response (using deflate or gzip)
         -K, --config FILE   Read config from FILE
             --connect-timeout SECONDS  Maximum time allowed for connection
             --connect-to HOST1:PORT1:HOST2:PORT2 Connect to host (network level)
         -C, --continue-at OFFSET  Resumed transfer OFFSET
         -b, --cookie STRING/FILE  Read cookies from STRING/FILE (H)
         -c, --cookie-jar FILE  Write cookies to FILE after operation (H)
             --create-dirs   Create necessary local directory hierarchy
             --crlf          Convert LF to CRLF in upload
             --crlfile FILE  Get a CRL list in PEM format from the given file
         -d, --data DATA     HTTP POST data (H)
             --data-raw DATA  HTTP POST data, '@' allowed (H)
             --data-ascii DATA  HTTP POST ASCII data (H)
             --data-binary DATA  HTTP POST binary data (H)
             --data-urlencode DATA  HTTP POST data url encoded (H)
             --delegation STRING  GSS-API delegation permission
             --digest        Use HTTP Digest Authentication (H)
             --disable-eprt  Inhibit using EPRT or LPRT (F)
             --disable-epsv  Inhibit using EPSV (F)
             --dns-servers   DNS server addrs to use: 1.1.1.1;2.2.2.2
             --dns-interface  Interface to use for DNS requests
             --dns-ipv4-addr  IPv4 address to use for DNS requests, dot notation
             --dns-ipv6-addr  IPv6 address to use for DNS requests, dot notation
         -D, --dump-header FILE  Write the received headers to FILE
             --egd-file FILE  EGD socket path for random data (SSL)
             --engine ENGINE  Crypto engine (use "--engine list" for list) (SSL)
             --expect100-timeout SECONDS How long to wait for 100-continue (H)
         -f, --fail          Fail silently (no output at all) on HTTP errors (H)
             --fail-early    Fail on first transfer error, do not continue
             --false-start   Enable TLS False Start.
         -F, --form CONTENT  Specify HTTP multipart POST data (H)
             --form-string STRING  Specify HTTP multipart POST data (H)
             --ftp-account DATA  Account data string (F)
             --ftp-alternative-to-user COMMAND  String to replace "USER [name]" (F)
             --ftp-create-dirs  Create the remote dirs if not present (F)
             --ftp-method [MULTICWD/NOCWD/SINGLECWD]  Control CWD usage (F)
             --ftp-pasv      Use PASV/EPSV instead of PORT (F)
         -P, --ftp-port ADR  Use PORT with given address instead of PASV (F)
             --ftp-skip-pasv-ip  Skip the IP address for PASV (F)
             --ftp-pret      Send PRET before PASV (for drftpd) (F)
             --ftp-ssl-ccc   Send CCC after authenticating (F)
             --ftp-ssl-ccc-mode ACTIVE/PASSIVE  Set CCC mode (F)
             --ftp-ssl-control  Require SSL/TLS for FTP login, clear for transfer (F)
         -G, --get           Send the -d data with a HTTP GET (H)
         -g, --globoff       Disable URL sequences and ranges using {} and []
         -H, --header LINE   Pass custom header LINE to server (H)
         -I, --head          Show document info only
         -h, --help          This help text
             --hostpubmd5 MD5  Hex-encoded MD5 string of the host public key. (SSH)
         -0, --http1.0       Use HTTP 1.0 (H)
             --http1.1       Use HTTP 1.1 (H)
             --http2         Use HTTP 2 (H)
             --http2-prior-knowledge  Use HTTP 2 without HTTP/1.1 Upgrade (H)
             --ignore-content-length  Ignore the HTTP Content-Length header
         -i, --include       Include protocol headers in the output (H/F)
         -k, --insecure      Allow connections to SSL sites without certs (H)
             --interface INTERFACE  Use network INTERFACE (or address)
         -4, --ipv4          Resolve name to IPv4 address
         -6, --ipv6          Resolve name to IPv6 address
         -j, --junk-session-cookies  Ignore session cookies read from file (H)
             --keepalive-time SECONDS  Wait SECONDS between keepalive probes
             --key KEY       Private key file name (SSL/SSH)
             --key-type TYPE  Private key file type (DER/PEM/ENG) (SSL)
             --krb LEVEL     Enable Kerberos with security LEVEL (F)
             --libcurl FILE  Dump libcurl equivalent code of this command line
             --limit-rate RATE  Limit transfer speed to RATE
         -l, --list-only     List only mode (F/POP3)
             --local-port RANGE  Force use of RANGE for local port numbers
         -L, --location      Follow redirects (H)
             --location-trusted  Like '--location', and send auth to other hosts (H)
             --login-options OPTIONS  Server login options (IMAP, POP3, SMTP)
         -M, --manual        Display the full manual
             --mail-from FROM  Mail from this address (SMTP)
             --mail-rcpt TO  Mail to this/these addresses (SMTP)
             --mail-auth AUTH  Originator address of the original email (SMTP)
             --max-filesize BYTES  Maximum file size to download (H/F)
             --max-redirs NUM  Maximum number of redirects allowed (H)
         -m, --max-time SECONDS  Maximum time allowed for the transfer
             --metalink      Process given URLs as metalink XML file
             --negotiate     Use HTTP Negotiate (SPNEGO) authentication (H)
         -n, --netrc         Must read .netrc for user name and password
             --netrc-optional  Use either .netrc or URL; overrides -n
             --netrc-file FILE  Specify FILE for netrc
         -:, --next          Allows the following URL to use a separate set of options
             --no-alpn       Disable the ALPN TLS extension (H)
         -N, --no-buffer     Disable buffering of the output stream
             --no-keepalive  Disable keepalive use on the connection
             --no-npn        Disable the NPN TLS extension (H)
             --no-sessionid  Disable SSL session-ID reusing (SSL)
             --noproxy       List of hosts which do not use proxy
             --ntlm          Use HTTP NTLM authentication (H)
             --ntlm-wb       Use HTTP NTLM authentication with winbind (H)
             --oauth2-bearer TOKEN  OAuth 2 Bearer Token (IMAP, POP3, SMTP)
         -o, --output FILE   Write to FILE instead of stdout
             --pass PASS     Pass phrase for the private key (SSL/SSH)
             --path-as-is    Do not squash .. sequences in URL path
             --pinnedpubkey FILE/HASHES Public key to verify peer against (SSL)
             --post301       Do not switch to GET after following a 301 redirect (H)
             --post302       Do not switch to GET after following a 302 redirect (H)
             --post303       Do not switch to GET after following a 303 redirect (H)
             --preproxy [PROTOCOL://]HOST[:PORT] Proxy before HTTP(S) proxy
         -#, --progress-bar  Display transfer progress as a progress bar
             --proto PROTOCOLS  Enable/disable PROTOCOLS
             --proto-default PROTOCOL  Use PROTOCOL for any URL missing a scheme
             --proto-redir PROTOCOLS   Enable/disable PROTOCOLS on redirect
         -x, --proxy [PROTOCOL://]HOST[:PORT]  Use proxy on given port
             --proxy-anyauth  Pick "any" proxy authentication method (H)
             --proxy-basic   Use Basic authentication on the proxy (H)
             --proxy-digest  Use Digest authentication on the proxy (H)
             --proxy-cacert FILE CA certificate to verify peer against for proxy (SSL)
             --proxy-capath DIR CA directory to verify peer against for proxy (SSL)
             --proxy-cert CERT[:PASSWD] Client certificate file and password for proxy (SSL)
             --proxy-cert-type TYPE Certificate file type (DER/PEM/ENG) for proxy (SSL)
             --proxy-ciphers LIST SSL ciphers to use for proxy (SSL)
             --proxy-crlfile FILE Get a CRL list in PEM format from the given file for proxy
             --proxy-insecure Allow connections to SSL sites without certs for proxy (H)
             --proxy-key KEY Private key file name for proxy (SSL)
             --proxy-key-type TYPE Private key file type for proxy (DER/PEM/ENG) (SSL)
             --proxy-negotiate  Use HTTP Negotiate (SPNEGO) authentication on the proxy (H)
             --proxy-ntlm    Use NTLM authentication on the proxy (H)
             --proxy-header LINE Pass custom header LINE to proxy (H)
             --proxy-pass PASS Pass phrase for the private key for proxy (SSL)
             --proxy-ssl-allow-beast Allow security flaw to improve interop for proxy (SSL)
             --proxy-tlsv1   Use TLSv1 for proxy (SSL)
             --proxy-tlsuser USER TLS username for proxy
             --proxy-tlspassword STRING TLS password for proxy
             --proxy-tlsauthtype STRING TLS authentication type for proxy (default SRP)
             --proxy-service-name NAME  SPNEGO proxy service name
             --service-name NAME  SPNEGO service name
         -U, --proxy-user USER[:PASSWORD]  Proxy user and password
             --proxy1.0 HOST[:PORT]  Use HTTP/1.0 proxy on given port
         -p, --proxytunnel   Operate through a HTTP proxy tunnel (using CONNECT)
             --pubkey KEY    Public key file name (SSH)
         -Q, --quote CMD     Send command(s) to server before transfer (F/SFTP)
             --random-file FILE  File for reading random data from (SSL)
         -r, --range RANGE   Retrieve only the bytes within RANGE
             --raw           Do HTTP "raw"; no transfer decoding (H)
         -e, --referer       Referer URL (H)
         -J, --remote-header-name  Use the header-provided filename (H)
         -O, --remote-name   Write output to a file named as the remote file
             --remote-name-all  Use the remote file name for all URLs
         -R, --remote-time   Set the remote file's time on the local output
         -X, --request COMMAND  Specify request command to use
             --resolve HOST:PORT:ADDRESS  Force resolve of HOST:PORT to ADDRESS
             --retry NUM   Retry request NUM times if transient problems occur
             --retry-connrefused  Retry on connection refused (use with --retry)
             --retry-delay SECONDS  Wait SECONDS between retries
             --retry-max-time SECONDS  Retry only within this period
             --sasl-ir       Enable initial response in SASL authentication
         -S, --show-error    Show error. With -s, make curl show errors when they occur
         -s, --silent        Silent mode (don't output anything)
             --socks4 HOST[:PORT]  SOCKS4 proxy on given host + port
             --socks4a HOST[:PORT]  SOCKS4a proxy on given host + port
             --socks5 HOST[:PORT]  SOCKS5 proxy on given host + port
             --socks5-hostname HOST[:PORT]  SOCKS5 proxy, pass host name to proxy
             --socks5-gssapi-service NAME  SOCKS5 proxy service name for GSS-API
             --socks5-gssapi-nec  Compatibility with NEC SOCKS5 server
         -Y, --speed-limit RATE  Stop transfers below RATE for 'speed-time' secs
         -y, --speed-time SECONDS  Trigger 'speed-limit' abort after SECONDS (default: 30)
             --ssl           Try SSL/TLS (FTP, IMAP, POP3, SMTP)
             --ssl-reqd      Require SSL/TLS (FTP, IMAP, POP3, SMTP)
         -2, --sslv2         Use SSLv2 (SSL)
         -3, --sslv3         Use SSLv3 (SSL)
             --ssl-allow-beast  Allow security flaw to improve interop (SSL)
             --ssl-no-revoke    Disable cert revocation checks (WinSSL)
             --stderr FILE   Where to redirect stderr (use "-" for stdout)
             --suppress-connect-headers  Suppress proxy CONNECT response headers
             --tcp-nodelay   Use the TCP_NODELAY option
             --tcp-fastopen  Use TCP Fast Open
         -t, --telnet-option OPT=VAL  Set telnet option
             --tftp-blksize VALUE  Set TFTP BLKSIZE option (must be >512)
             --tftp-no-options  Do not send TFTP options requests
         -z, --time-cond TIME   Transfer based on a time condition
         -1, --tlsv1         Use >= TLSv1 (SSL)
             --tlsv1.0       Use TLSv1.0 (SSL)
             --tlsv1.1       Use TLSv1.1 (SSL)
             --tlsv1.2       Use TLSv1.2 (SSL)
             --tlsv1.3       Use TLSv1.3 (SSL)
             --tls-max VERSION  Use TLS up to VERSION (SSL)
             --trace FILE    Write a debug trace to FILE
             --trace-ascii FILE  Like --trace, but without hex output
             --trace-time    Add time stamps to trace/verbose output
             --tr-encoding   Request compressed transfer encoding (H)
         -T, --upload-file FILE  Transfer FILE to destination
             --url URL       URL to work with
         -B, --use-ascii     Use ASCII/text transfer
         -u, --user USER[:PASSWORD]  Server user and password
             --tlsuser USER  TLS username
             --tlspassword STRING  TLS password
             --tlsauthtype STRING  TLS authentication type (default: SRP)
             --unix-socket PATH    Connect through this Unix domain socket
             --abstract-unix-socket PATH Connect to an abstract Unix domain socket
         -A, --user-agent STRING  Send User-Agent STRING to server (H)
         -v, --verbose       Make the operation more talkative
         -V, --version       Show version number and quit
         -w, --write-out FORMAT  Use output FORMAT after completion
             --xattr         Store metadata in extended file attributes
         -q, --disable       Disable .curlrc (must be first parameter)
- curl重要参数
    - -H "Content-Type:application/json" 消息头设置
    - -u username:password 用户认证
    - -d 要发送的post数据@file 表示来自于文件
    - --data-urlencode 'page_size=50' 对内容进行url编码
    - -G 把data数据当成get请求的参数发送，长与--data-urlencode结合使用
    - -o 写文件
    - -x 代理http代理 socks5代理
    - -v verbose打印更详细日志
    - -s关闭一些提示输出
- curl命令实战

        url=http://www.baidu.com
        ## get请求加json解析 
        curl -s 'https://xueqiu.com/stock/search.json?code=sogo&size=3&page=1' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Accept: application/json, text/plain, */*' -H 'Sec-Fetch-Dest: empty' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36' -H 'elastic-apm-traceparent: 00-760301b0a132e9a4c0f5ac7448a3419e-8823be75504fc61f-00' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Referer: https://xueqiu.com/k?q=sogo' -H 'Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7' -H 'Cookie: device_id=24700f9f1986800ab4fcc880530dd0ed; cookiesu=841584103115161; aliyungf_tc=AQAAAIPytE8aVQoAXhjf3cw3R+j5DD/s; acw_tc=2760824b15851452106833674e25941ad47588d5d7ded79b38a04dad8f9444; xq_a_token=2ee68b782d6ac072e2a24d81406dd950aacaebe3; xqat=2ee68b782d6ac072e2a24d81406dd950aacaebe3; xq_r_token=f9a2c4e43ce1340d624c8b28e3634941c48f1052; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTU4NzUyMjY2MSwiY3RtIjoxNTg1MTQ1MTYxMDIwLCJjaWQiOiJkOWQwbjRBWnVwIn0.TPrw6_M2Th9QTVz5spwUybqN1790nJANu9kxXl4GfNb1eQ2p2zD43CStgogOGQ8yRXYmSCfURp0343wgjnnCdnQX5698Jl-brdP94wiYKwv11q8QjBYMXFWJGRj0g69C2nxVrRF8K-ETGEked3KjYfk8Xy2wPuZtyGUhORWeCvMhmBdcRKIlWj4d7wp-w_LjMbSLigJAT29F03wBZIxR0r3eMNUhUsXh8dCsWNb6wzhtg8dT4gcd91mQmR5ToR_SFrzQfOopY4vQGcaOHWaAwUMPLUopZwD4ajWzm1kpoBZnf_n_9uBfT4j0nGk95E8J8EmTfBlq-1p019xkhgp87w; u=431585145210698; Hm_lvt_1db88642e346389874251b5a1eded6e3=1583285031,1584102200,1585145180; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1585145192' --compressed | jq
        {
          "q": "sogo",
          "page": 1,
          "size": 3,
          "stocks": [
            {
              "code": "SOGO",
              "name": "搜狗",
              "enName": "",
              "hasexist": "false",
              "flag": null,
              "type": 0,
              "stock_id": 1029472,
              "ind_id": 0,
              "ind_name": "通讯业务",
              "ind_color": null,
              "_source": "sc_1:1:sogo"
            }
          ]
        }
        
        
        #post请求
        curl 'http://sonarqube.testing-studio.com:9000/api/authentication/login' -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' -H 'Accept: application/json' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Origin: http://sonarqube.testing-studio.com:9000' -H 'Referer: http://sonarqube.testing-studio.com:9000/sessions/new' -H 'Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7' -H 'Cookie: _ga=GA1.2.232181868.1566982077; experimentation_subject_id=IjNlYzgxODQ1LTU2MDAtNGIyNy1iNTgzLTE1MzRkY2IwMDI0ZSI%3D--b1f29d33f6a2c85a81be66e4774d437f710c102f; _gid=GA1.2.482544306.1585051015' --data 'login=admin&password=1234' --compressed --insecure
        
        #百度的一个url提交脚本
        curl -H 'Content-Type:text/plain' --data-binary @urls.txt "http://data.zz.baidu.com/urls"
        
        #对参数编码并发送get请求
            curl -G $url  \
                --data-urlencode "current=$current" \
                --data-urlencode "pageSize=$pageSize" 
        
        
        #认证与put上传都ElasticSearch里
            curl -X PUT "$ES_HOST/$index/_doc/$id?pretty" \
                --user username:password \
                -H 'Content-Type: application/json' \
                -d "$content"
        
        
        #查看邮箱
        curl -s --user $mail_username:$mail_password "imaps://imap.exmail.qq.com/inbox?all"

`

### 代理工具
- 常用代理工具
    - 代理工具：charles、burpsuite、fiddler、mitmproxy
    - 高性能代理服务器：squid、dante
    - 反向代理：nginx
    - 流量转发与复制：em-proxy、gor、iptable、nginx
    - socks5代理：ssh -d参数
- nc(netcat):一个简单而有用的工具，透过使用TCP或UDP协议的网络连接去读写数据
    - 使用nc简易演示代理实现
    - nc -lk 8080 < /tmp/fifo | sed -l -e 's/^Host.*/Host:site.baidu.com/' | tee -a /tmp/req.log | nc site.baidu.com 80 | tee -a /tmp/res >/tmp/fifo
            
            nc -lk 8080</tmp/fifo \
            | sed -l -e 's/^Host.*/Host:
            site.baidu.com/' \
            | tee -a /tmp/req.log \
            | nc site.baidu.com 80 \
            | tee -a /tmp/res> /tmp/fifo
- 优秀代理工具必备特性
    - 代理功能：http/https、socks5
    - 请求模拟工具：拼装请求、重放请求、重复请求
    - 网络环境模拟：限速、超时、返回异常
    - mock：请求修改、响应修改
    - fake：用测试环境替代真实环境
- 推荐工具
    - charles：开发/测试工程师必备
    - mitmproxy：测试开发工程师必备
    - zap：测试工程师安全测试工具
    - burpsuite：黑客必备渗透测试工具
    - fiddler：跨平台支持不好，不推荐
    - postman：代理功能太弱，不推荐

### http/https抓包分析 
- 代理配置步骤
    - 配置代理
    - 获取证书:http://chls.pro/ssl
    - 安装证书:mac上安装并设置信任
    - 信任证书
- mock实战-数据修改演示
    - 雪球股票展示测试
    - 数据修改演示
    - 选择Tools-Rewrite settings，以Hogwarts为例
- mock实战-数据加倍演示
    - 雪球股票展示测试
    - 数据加倍演示
    - 操作：
        - vi /tmp/stock_demo
        - raw=$(cat /tmp/stock_demo)
        - raw=$(echo "$raw" | jq '.data.items+=.data.items' | jq '.data.items_size+=.data.items_size')
        - echo "$raw" > /tmp/mock.json
        - 针对某一个接口，选择Map Local，Map To的local path填写/tmp/mock.json
- 使用总结
    - rewrite：简单mock
    - map local：复杂mock
    - map remote：整体测试环境
    
### http协议讲解
- http报文结构
    - 请求报文：请求行、首部行、实体主体
    - 响应报文：状态行、首部行、实体主体
- 请求报文方法：
    - OPTION/GET/POST/HEAD/PUT/DELETE/TRACE/CONNECT
- 常见状态码
    - 1xx：通知信息。
    - 2xx：成功。
    - 3xx：重定向。
    - 4xx：客户端错误。
    - 5xx：服务端错误
- curl命令：后面加上 -v 2>&1 >1.log

### session、cookie、token区别解析
- session与cookie区别
    - cookie：浏览器接受服务器的Set-Cookie指令，并把cookie保存到电脑上，
    每一个网站保存的cookie只作用于自己的网站
    - session：数据存储到服务器，只把关联数据的一个加密串放到cookie中标记
- session与token的区别
    - token是一个用户请求时附带的请求字段，用于验证身份与权限
    - session可以基于cookie，也可以基于query参数，用于关联用户相关数据
    - 跨端应用的时候，比如android原生系统不支持cookie
        - 需要用token识别用户
        - 需要把sessionid保存到http请求中的header或者query字段中
### mitmproxy抓包工具
- 类似于WireShark、Filddler，并且它支持抓取HTTP和HTTPS协议的数据包
- https://www.jianshu.com/p/036e5057f0b9
- 有两个非常有用的组件，一个mitmdump，它是mitmproxy的命令行接口，利用它可以对接python脚本；另一个是mitmweb，它是一个web程序，通过它可以清楚的观察mitmproxy捕获的数据情况，优点类似于Chrome浏览器。