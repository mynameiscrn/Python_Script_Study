"""
@Author:陈锐安
@Time:2022/1/11 0011 上午 9:19
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
"""
局部变量:函数内部定义的变量
全局变量:函数外部定义的变量
"""
sum_global = 1

def add(*args):
    print(args)
    global sum_global
    sum_num = 0 #局部变量.只有函数内部可用
    for item in args:
        sum_num += item
        sum_global += 1 #全局变量在函数内部可以使用.但不可以修改.需要用global申明为全局变量
    return sum_num

def add1():
    return sum_global+1

def add2():
    global sum_global
    sum_global += 1
add2()
print(sum_global)

# sum_global += add(1,3,4,5,6)
# sum_global += add(100,200,300,400)

print("---------------------------拆包------------------------------")
num_list = [100,200,300,400]

def add123(a,b,c,d):
    sum_num = a+b+c+d
    print(sum_num)
add123(*num_list)

def add321(*args):
    sum_num = 0
    for val in args:
        sum_num += val
    print(sum_num)
add321(*num_list)

def print_info(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key,value)
person_info = {"name":"xx","age":20,"city":"北京"}
print_info(**person_info)