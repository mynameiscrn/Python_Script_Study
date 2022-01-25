"""
@Author:陈锐安
@Time:2022/1/10 0010 下午 3:42
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
count = 1

while count <= 10:
    print(count)
    count += 1
    if count == 2:
        continue
    print('hello python '+str(count))
    if count == 5:
        print("已经50次了,再见!")
        break