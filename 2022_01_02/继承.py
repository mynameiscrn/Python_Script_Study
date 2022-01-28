"""
@Author:陈锐安
@Time:2022/1/28 0028 上午 9:29
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
class Base:
    def __init__(self,name):
        print("初始化对象:{}!",format(self))
        self.name = name

    def eat(self):
        print("吃")

    def sleep(self):
        print("睡")

    def hawl(self):
        print("嚎")

class Cat(Base):
    def __init__(self,name,sex):
        super().__init__(name)
        self.self = sex

    def climb(self):
        print("Cat会爬树")
        self.eat()

    def sleep(self):
        super().sleep()
        print("我是用爸爸睡觉的姿势,顺便再加一个姿势!!")

c = Cat("英短","母")
c.sleep()