"""
@Author:陈锐安
@Time:2022/1/11 0011 上午 11:15
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
import os

"""
__file__:当前文件名
获取当前文件的绝对路径:os.path.abspath(__file__)
获取当前文件所在目录:os.path.dirname(__file__)
路径拼接:os.path.join
"""
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))
print(os.path.dirname(os.path.dirname(r'D:\Python_Script\2021_12_31\pymodule\路径处理.py')))

#路径拼接
base_dir = os.path.abspath(os.path.dirname(__file__))
res = os.path.join(base_dir,"hello.py.py")
print(res)
print(os.path.isdir(r'D:\Python_Script\2021_12_31\pymodule'))
print(os.listdir(r'D:\Python_Script\2021_12_31\pymodule'))

print(os.path.realpath(__file__))