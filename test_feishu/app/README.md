这样实现的意义有什么好处，个人认为有如下的几点优势：

1、父类层只编写selenium2,appium共同可以使用到的方法；

2、在对象层中，selenium2和appium完全隔离开，selenium2写web的,appium写app的

3、在测试层中，也是完全分开的，web和app各自执行自己的case，完全不影响