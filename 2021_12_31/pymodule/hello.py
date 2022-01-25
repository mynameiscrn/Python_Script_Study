"""
@Author:陈锐安
@Time:2022/1/11 0011 上午 11:14
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
import sys
LEVEL = 1
def get_level():
    print(LEVEL)

if __name__ == '__main__':
    print("我没有被引入,我是在当前文件被引入")
    print(range(3))
    for i in range(3):
        print(i)
    for value in sys.path:
        print(value)