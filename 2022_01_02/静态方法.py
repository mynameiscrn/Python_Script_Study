"""
@Author:陈锐安
@Time:2022/1/28 0028 上午 9:30
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
def hello():
    print("hello")

class Dog:
    def bark(self):
        print("叫")

    @classmethod
    def set_kind(cls):
        cls.kind = "狗"

    @staticmethod
    def hello(flag=True):
        print("hello,dog!!")

Dog.hello()
d = Dog()
d.hello()
