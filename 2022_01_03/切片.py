"""
@Author:陈锐安
@Time:2022/1/28 0028 下午 2:17
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
L = ['Michae1','Sarah','Tracy','Bob','Jack']
print(L[0])
print(L[1])
print(L[2])
print('*******************用循环的方式*********************')
for i in range(3):
    print(L[i])
print('*******************用切片的方式*********************')
print(L[0:3])
print(L[:3])
print(L[-1])
print(L[-2:])
print(L[-2:-1])

print('*******************切片十分有用*********************')
L = list(range(100))
print(L)
print(L[:10])
print(L[-10:])
print('**********这个没看懂***********')
print(L[1])
print(L[10:20])
print('**********前10个数,每两个取一个**********')
print(L[:10:2])