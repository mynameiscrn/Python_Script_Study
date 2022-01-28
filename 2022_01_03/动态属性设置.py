"""
@Author:陈锐安
@Time:2022/1/28 0028 上午 10:33
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
class People:
    def __init__(self,name):
        self.name = name
p = People("xj")
ss = People("xx")
#hasattr,getattr,setattr,delattr

res = hasattr(People,"name")
print(res)
res = hasattr(p,"name")
print(res)

s = getattr(p,"name")
print(s)

#setattr  如果属性存在,修改属性值,如果不存在,添加属性
setattr(People,"kind","黄种人")
print(People.kind)
print(p.kind)

setattr(p,"kind","黑人")
print(p.kind)
print(People.kind)

#delattr,删除属性
delattr(p,"name")
try:
    print(p.name)
except:
    print("该属性已经被删除了")

s = isinstance(p,People)
print(s)

print("*****************is********************")
print(id(p))
print(id(ss))
print(ss is None)
print(type(ss))
print(type(ss) is People)