"""
@Author:陈锐安
@Time:2022/1/11 0011 下午 1:45
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
#r'D:\soft\chromedriver_win32\chromedriver.exe'
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
#创建Webdriver的对象,指明使用chrome浏览器驱动,当然这里还有很多驱动
#wd = webdriver.Chrome(r'D:\soft\chromedriver_win32\chromedriver.exe')
#wd = webdriver.Chrome(service=Service(r'D:\soft\chromedriver_win32\chromedriver.exe'))
"""
因为，Selenium会自动在环境变量 Path 指定的那些目录里查找名为chromedriver.exe 的文件。

一定要注意的是， 加入环境变量 Path 的，

不是浏览器驱动全路径，比如 d:\webdrivers\chromedriver.exe

而是 浏览器驱动所在目录，比如 d:\webdrivers

添加完环境变量后需要重启pycharm或者是cmd
"""
wd = webdriver.Chrome()
# 设置最大等待时长为 10秒
wd.implicitly_wait(10)
#调用Webdriver对象的get方法,可以让浏览器打开指定网址
wd.get('https://www.baidu.com')

kw = wd.find_element(By.ID,'kw')
kw.send_keys('陈锐安')
time.sleep(3)
#清理掉输入的内容
kw.clear()
time.sleep(3)
kw.send_keys('刘备')
time.sleep(3)
su = wd.find_element(By.ID,'su')
print(su.get_attribute('value'))
print(su.get_attribute('outerHTML'))     #获取自己
print(su.get_attribute('innerHTML'))     #应该是获取所有的子元素
"""
通过WebElement对象的 text 属性，可以获取元素 展示在界面上的 文本内容。

但是，有时候，元素的文本内容没有展示在界面上，或者没有完全完全展示在界面上。 这时，用WebElement对象的text属性，获取文本内容，就会有问题。

出现这种情况，可以尝试使用 element.get_attribute('innerText') ，或者 element.get_attribute('textContent')
"""
su.click()
#wd.quit()