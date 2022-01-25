"""
@Author:陈锐安
@Time:2022/1/11 0011 下午 3:04
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 加上参数，禁止 chromedriver 日志写屏,在pycharm并不会打日志,在cmd运行的话就会打印
options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

wd = webdriver.Chrome(
    options=options  # 这里指定 options 参数
)

#wd = webdriver.Chrome()
wd.get('https://test.taotaoshi.cn/index.php?g=Pfs&m=Public&a=login')
Business_License = wd.find_element(By.NAME,'business_no')
Password = wd.find_element(By.NAME,'password')
loginBtn = wd.find_element(By.CLASS_NAME,"loginBtn")
Business_License.send_keys('000000000000001')
Password.send_keys('a111111')
loginBtn.click()