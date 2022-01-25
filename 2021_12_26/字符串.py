"""
@Author:陈锐安
@Time:2021/12/24 0024 下午 3:37
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
s = ""
s1 = None  #不代表任何一个数据类型
print(s)
print(s1)
print(type(s1))

person_info = '我是陈锐安,准备过元旦节了'
print(person_info)
person_info = '我是陈锐安,我喜欢\'女生\''
print(person_info)

print(person_info[6])         #我
print(person_info[-1])        #'

print(person_info[0:6])       #我是陈锐安,
print(person_info[:7])        #我是陈锐安,我
print(person_info[:7:2])      #我陈安我
print(person_info[7:1:-2])    #喜,锐是   xxxxxxxxxxxxxxxxx 1是第二位,所以答案是喜,锐
print(person_info[-1:-10:-1]) #'生女'欢喜我,安
print(person_info[:])         #我是陈锐安,我喜欢'女生'
print(person_info[::-1])      #'生女'欢喜我,安锐陈是我


print("******************* 常用方法/功能 *****************************")
#find(子字符串)正向查找子字符串,找到返回的值都是>=0,没有找着就是-1
index = person_info.find("我是小简老师111")
print(index)
#count(字符/字符串)统计在原字符串当中出现的次数
count = person_info.count("我")
print(count)
#upper()将字符串的字母转换成大写.重新生成一个字符串,不会修改原来的字符串
res = "app".upper()
print(res)
person_info = '我是小简老师,我喜欢"python30期",我今天跟你们过节呢!'
#split()分隔.分隔符
#sep:分隔符.不会出现在分割后的数据当中
#maxsplit:1 分割的次数
str_pian = person_info.split(",")
print(person_info)
print(str_pian)

#join() 拼接.按照拼接符将其拼接起来
#把支离破碎的几个字符串,拼接成一个完整的字符串
#1\拼接符:一定是字符串
ss = "   ".join(str_pian)  #按照一定的规律去拼接 列表里的字符串
print(ss)

#替换操作
#replace(原字符串当中要被替换,新的字符)
sss = person_info.replace("我","你")
print(person_info)
print(sss)
'''
age = int(input("年龄:"))
print(age)
print(type(age))
name = input("name:")

print("我的年龄是:{}岁,我的名字是:{}".format(age,name))

print("我的年龄是:{1}岁,我的名字是:{2},我的老师是:{2}.我喜欢干什么:{0}".format("睡觉",age,name))
'''

print("hello,world! \n hello,py30!")
print('hello,world! \n hello,py30!')

print("hello world! \t hello,py30!")
print('hello world! \t hello,py30!')

print(r" hello,world! \n hello,py30!")


str1 = " hello,world!!!"
str2 = "hello,python!"
str3 = "No!!!"
int1 = 20
print(str1+str2+str3+str(int1))