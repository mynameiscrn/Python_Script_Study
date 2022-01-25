"""
@Author:陈锐安
@Time:2022/1/10 0010 下午 3:41
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
list_p = ["Mr 张","荒年","Madao","吴亦凡","深夜吃糖","罗志祥"]
for item in list_p:
    print(item)

print(list(range(6)))

for index in list(range(len(list_p))):
    print(index)
    print(list_p[index])


print("---------------------字典开始方法一--------------------------")

person_info = {"sex":"男","tzh":"帅,有钱,会哄人","age":30}
for key in person_info.keys():
    print(key)
    print(person_info[key])

print(type(person_info.keys()))


print("---------------------字典开始方法二--------------------------")
print(person_info.items())
print(list(person_info.items()))
a,b = list(person_info.items())[0]
a,b,c = ('chen','rui','an')
print("a="+a+",b="+b+",c="+c)

for key,value in person_info.items():
    print(key,value)