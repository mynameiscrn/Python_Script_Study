"""
@Author:陈锐安
@Time:2022/1/11 0011 下午 3:29
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import time
#pip install pypiwin32
import win32gui
import win32con
import os


def upload_file(file_path):
    '''
    :param file_path:上传文件的路径
    :return:
    '''
    dialog = win32gui.FindWindow("#32770", "打开")
    comboxex32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
    combox = win32gui.FindWindowEx(comboxex32, 0, "ComboBox", None)
    edit = win32gui.FindWindowEx(combox, 0, "Edit", None)
    button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&0)")
    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, file_path)
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)



# 加上参数，禁止 chromedriver 日志写屏,在pycharm并不会打日志,在cmd运行的话就会打印
options = webdriver.ChromeOptions()
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])

wd = webdriver.Chrome(
    options=options  # 这里指定 options 参数
)
wd.maximize_window()
# 设置最大等待时长为 10秒
wd.implicitly_wait(10)
#wd = webdriver.Chrome()
wd.get('https://test.taotaoshi.cn/index.php?g=Pfs&m=Public&a=login')
#开始登陆
Business_License = wd.find_element(By.NAME,'business_no')
Password = wd.find_element(By.NAME,'password')
loginBtn = wd.find_element(By.CLASS_NAME,"loginBtn")
Business_License.send_keys('000000000000001')
Password.send_keys('a111111')
loginBtn.click()
#登陆结束
chanpin = wd.find_element(By.XPATH,"//dt[contains(text(),'产品管理')]")
chanpin.click()
chanpinlink = wd.find_element(By.LINK_TEXT,'产品管理')
chanpinlink.click()
#添加商品开始
iframe1 = wd.find_element(By.XPATH,'//iframe[@src="https://test.taotaoshi.cn/index.php?g=Pfs&m=Goods&menuid=342"]')
wd.switch_to.frame(iframe1)
tianjiachanpin = wd.find_element(By.PARTIAL_LINK_TEXT,'添加产品')
tianjiachanpin.click()
uploadphoto = wd.find_elements(By.ID,'thumtop')
wd.find_element(By.CLASS_NAME,'add-img-btn').click()
time.sleep(1)
upload_file(r'D:\123.png')
#os.system(r"D:\soft\uploadphoto.exe")
wd.find_element(By.CLASS_NAME,'base64-btn2').click()
wd.find_element(By.CLASS_NAME,'select-fl').click()
time.sleep(0.3)
wd.find_element(By.XPATH,'//span[@jq="2349"]').click()
clickok = wd.find_element(By.XPATH,'//input[@type="button" and @value="确定"]')
clickok.send_keys(Keys.ENTER)
wd.find_element(By.ID,'title').send_keys('陈锐安测试1')
wd.find_element(By.XPATH,'//*[@id="price_grade1"]').send_keys(Keys.ENTER)
wd.find_element(By.XPATH,'//*[@id="queren_grade"]').click()
wd.find_element(By.XPATH,'//input[@placeholder="请输入单位"]').send_keys('个')
wd.find_element(By.XPATH,'//*[@id="myform"]/div[14]/div/div/table/tbody/tr/td[2]/input').send_keys('0.01')
wd.find_element(By.XPATH,'//input[@placeholder="请输入库存数量"]').click()
wd.execute_script('document.querySelector("#myform > div:nth-child(12) > div > input").value=""')
# wd.find_element(By.XPATH,'//input[@placeholder="请输入库存数量"]').clear()
wd.find_element(By.XPATH,'//input[@placeholder="请输入库存数量"]').send_keys('1000')
# wd.find_element(By.XPATH,'//*[@id="myform"]/div[24]/div/div[2]/div/ins').send_keys(Keys.ENTER)
wd.find_element(By.XPATH,'//*[@id="myform"]/div[24]/div/div[2]/div').click()
wd.find_element(By.XPATH,'//*[@id="myform"]/div[24]/div/div[3]/div').click()
wd.find_element(By.XPATH,'//*[@id="ps_str"]/div[1]/div').click()
wd.find_element(By.XPATH,'//*[@id="ps_str"]/div[2]/div').click()
wd.find_element(By.ID,'save').click()
WebDriverWait(wd, 10).until(EC.alert_is_present()).accept()


'''
wd.switch_to.default_content()
iframe1 = wd.find_element(By.XPATH,'//iframe[@src="https://test.taotaoshi.cn/index.php?g=Pfs&m=Goods&menuid=342"]')
wd.switch_to.frame(iframe1)
tianjiachanpin = wd.find_element(By.PARTIAL_LINK_TEXT,'添加产品')
tianjiachanpin.click()
'''

#校验图片有没有上传成功
time.sleep(2)
wd.switch_to.default_content()
iframe1 = wd.find_element(By.XPATH,'//iframe[@src="https://test.taotaoshi.cn/index.php?g=Pfs&m=Goods&menuid=342"]')
wd.switch_to.frame(iframe1)
tbody = wd.find_elements(By.TAG_NAME,'tbody')
img = wd.find_element(By.XPATH,'//tbody/tr[1]/td[3]/a/img')
img_url = wd.find_element(By.XPATH,'//tbody/tr[1]/td[3]/a/img').get_attribute('src')
get_img = requests.get(img_url)
if get_img.status_code == 200:
    print("图片上传成功")
else:
    print('图片上传失败')
