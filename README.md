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