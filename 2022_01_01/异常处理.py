"""
@Author:陈锐安
@Time:2022/1/21 0021 下午 5:36
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
import os
filepath = os.path.abspath(__file__)
newfilepath = os.path.join(os.path.dirname(filepath),"chen.py")
try:
    fs = open(newfilepath,'r',encoding='utf-8')
except KeyError:
    pass
except FileNotFoundError as e:
    print("进入了这个异常的捕获")
    print(e)