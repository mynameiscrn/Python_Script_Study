"""
@Author:陈锐安
@Time:2021/12/29 0029 下午 1:44
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""

score = input("本次考试成绩分数为:")

if int(score) == 100:
    print("一个么么哒!")
    print("干的漂亮")

if int(score) > 60:
    print("及格")
else:
    print("不及格")

if 85<= int(score) <= 100:
    print("A")
elif 75 <= int(score) <= 85:
    print("B")
elif 60 <= int(score) <= 75:
    print("C")
else:
    print("D")
