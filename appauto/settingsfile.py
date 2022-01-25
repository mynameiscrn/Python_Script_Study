"""
@Author:陈锐安
@Time:2022/1/4 0004 下午 5:48
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
from appium import webdriver
from time import sleep

desired_caps = dict()
# 平台名字,大小写不敏感
desired_caps['platformName'] = 'Android'
# 系统版本
desired_caps['platformVersion'] = '5.1'
# 设备名字
desired_caps['deviceName'] = '127.0.0.1:62025'
# 要打开的app包名
desired_caps['appPackage'] = 'com.android.settings'

# 不需要每次都装app
desired_caps['noReset'] = True
desired_caps['fullReset'] = 'fullReset'
# 要打开的界面名
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(5)


driver.quit()