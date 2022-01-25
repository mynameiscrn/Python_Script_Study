"""
@Author:陈锐安
@Time:2021/12/24 0024 上午 11:52
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
num1 = 10
num2 = 52

res = num1 + num2
print(res)

res2 = num1 - num2
print(res2)

res3 = num1 * num2
print(res3)

res4 = num1 / num2
print(res4)

print(100/5)

#这种情况会报错的,分母不能为0
#print(100/0)

#求余
res5 = num1 % num2
print(res5)
print(1%2)
print(5%2)
print(6%2)
print(2%6)

res6 = (num1 * num2) + (num1 * num2)
print(res6)

print("*****************************************")

sum = 0
print(sum)
sum += 120
print(sum)
sum += 80
print(sum)
sum += 200
print(sum)
print(sum)

sum -= 200
print("我最终为520支付的人民币为:")
print(sum)

print("**************  比较运算符  ******************")
my_money = 2000
you_money = 520

print(my_money == you_money)
print(my_money != you_money)
print(my_money > you_money)
print(my_money >= you_money)
print(my_money < you_money)
print(my_money <= you_money)


# print("*************  逻辑运算符  ***************")
# age = input("请输入相亲候选人的年龄:")
# height = input("请输入你相亲候选人的身高:")
# salary = input("请输入相亲候选人的收入:")
# print("年龄为:"+age+",身高为:"+height+",收入为:"+salary)
#
# res = (int(age) > 20) and (int(height) > 160) and (int(salary) > 8000)
# print(res)


age = "21"
res2 = not(int(age) > 20)
print(res2)



