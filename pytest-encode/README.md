###打包：
执行python setup.py sdist bdist_wheel

###dist文件
-tar：源码包
-whl：安装包

##本机安装
pip install pytest-encode/dist/pytest_encode-1.0-py3-none-any.whl

###在其他项目中安装自定义包：
pip install dist/pytest_encode-1.0-py3-none-any.whl

###在其他项目中卸载自定义包：
pip uninstall pytest-encode

###在其他项目中引入已安装的包
from pytest_encode import logger