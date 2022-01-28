"""
@Author:陈锐安
@Time:2022/1/21 0021 下午 5:36
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
class Dog:
    kind = "狗"

    def __init__(self,name,kind,age):
        self.dog_name = name
        self.dog_kind = kind
        self.dog_age = age
        self.kind = "chenruian"

    #声明为类的方法
    @classmethod
    def set_kind(cls):                #cls代表当前类.可以访问类属性的
        print("我是类行为")
        print(cls.kind)

    #叫 - 方法
    def bark(self):
        print("旺旺旺")
        print(self.dog_name)

    def eat(self):
        print("吃狗粮")

    def run(self):
        print(self.dog_name,"跑起来")

cqg = Dog("小金毛","漂亮国和小日本的混血","3个月")
print("cqg对象的名字:",cqg.dog_name)
cqg.run()
print(cqg.kind)
print("----------------------------")
print(Dog.kind)
cqg.set_kind()
Dog.set_kind()