"""
@Author:陈锐安
@Time:2021/12/24 0024 下午 3:36
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""

"""
字符串：取值、切片、find\count、转义
1、str1 = 'python cainiao 666'
2、卖橘子的计算器：写一段代码，提示用户输入橘子的价格，和重量，最后计算出应该支付的金额！（不需要校验数据，都传入数字就可以了。）
3、my_hobby = "Never stop learning!"
"""

str1 = 'python cainiao 666'
print(str1[4])
str2 = str1
index = len(str1) / 2
print(int(index)-1)
print(type(index))
index = int(index) - 1
print(str1[index])

my_hobby = "Never stop learning"
print(my_hobby)

print(my_hobby[-2:])
print(my_hobby[-1:-3:-1])
print(my_hobby[-1:-4:-1])


