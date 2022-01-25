"""
@Author:陈锐安
@Time:2022/1/14 0014 下午 3:41
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()
wd.get("http://www.baidu.com")
#wd.maximize_window()        #把窗口进行最大化
sleep(2)
wd.find_element(By.CSS_SELECTOR,'#kw').send_keys('selenium 自学网')
#当前页面,5s之内,每隔0.5s检测一次id=su的元素.直到查找到
#显示等待
#搜索框元素的显示等待 until判断条件。跟进id进行定位，调用EC条件类
element = WebDriverWait(wd,30,0.5).until(EC.presence_of_element_located((By.ID,'su123')))
element.click()

