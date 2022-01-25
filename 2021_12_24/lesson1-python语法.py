"""
@Author:陈锐安
@Time:2021/12/24 0024 上午 11:34
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""

from appium import webdriver
print("人生苦短,我选python")

caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "10"
caps["deviceName"] = "AF8YVB1731006352"
caps["appPackage"] = "com.tts.mobilecashier"
caps["appActivity"] = ".ui.activity.SplashActivity"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.quit()





# today = "hello,nmb,py30,xj!"
# py30 = "good"
# hello_world = "hello,world!"
#
# print(today)
# print(today)
# print(today)
# print(today)
# print(today)
#
# age = 18.5
# age_str = "18.5"
# age_str2 = '18.5'
# person_info = "你好,我叫xxx,我来自xxx,我现在工作"\
# "是XXX,我的项目是XXX,我负责的XXX"
# print(age)
# print(age_str)
# print(age_str2)
# print(person_info)
#
# person_info2 = """
# 你好,我叫xxx
# 我来自xxx,我现在工作xxx
# 我的项目是xxx,我负责的xxx
# 我现在的技能是...
# """
# print(person_info2)
# is_ten_oclock = False
# after_ten = True
#
# print(is_ten_oclock)
# print(after_ten)
#
# money = 20
#
# print(type(money))
# print(type(age))
# print(type(age_str))
# print(type(age_str2))
# print(type(is_ten_oclock))
# print(type(after_ten))
# print("代码到此结束,下午再战~@")