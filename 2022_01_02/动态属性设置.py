"""
@Author:陈锐安
@Time:2022/1/28 0028 上午 9:29
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
class People:
    def __init__(self,name):
        self.name = name

p = People("xj")
print(p.name)
p.name = "黄花菜"
print(p.name)
p.sex = "女"
print(p.sex)

res = hasattr(People,"name")
print(res)
res = hasattr(p,"name")
print(res)