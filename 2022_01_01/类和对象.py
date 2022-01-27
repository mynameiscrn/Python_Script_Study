"""
@Author:陈锐安
@Time:2022/1/21 0021 下午 5:36
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
class Dog:
    kind = "狗"
    def __init__(self,name,kind,age):
        self.name = name
        self.kind = kind
        self.age = age

    def bark(self):
        print("汪汪汪")

    def eat(self):
        print("吃狗粮")

    def run(self):
        print("self本身:",self)
        print("跑起来")

cqg = Dog("纸老虎","漂亮国和小日本的混血","3个月")
print("对象本身:",cqg)
print(cqg.kind)
cqg.run()
cqg.eat()
cqg.bark()
print(cqg.kind)
print("cqg对象的名字:",cqg.name)

print("**********************************")
you_jm = Dog("小金","金毛","1岁")
you_jm.run()
you_jm.bark()
print(you_jm.kind)

print("**********************************")
print(Dog.eat())
print(Dog.kind)