"""
@Author:陈锐安
@Time:2022/1/10 0010 下午 5:21
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
def get_money():
    print("取了500万!")
    print("我笑醒了!")
    print("不用上班了!")
get_money()

def get_money_V2(cardNum,passwd,count):
    if len(cardNum) < 10 :
        print("卡号错了,再见!")
    if len(passwd) != 6:
        print("密码长度出错,再见!")
    if int(count) % 100 != 0:
        print("金额不为100的整数倍!")

get_money_V2("12345678900","4567","500")

print("--------------------带参数的函数-------------------------")
def get_money_V3(cardNum,passwd="123456",count=1000):
    if len(cardNum) < 10:
        print("卡号错了,再见!")
    if len(passwd) != 6:
        print("密码长度出错,再见!")
    if int(count) % 100 != 0:
        print("金额不为100的整数倍!")
    else:
        print(count)

get_money_V3("123456789")
get_money_V3("12345678900","123000")
get_money_V3("12345678900",count=2000)


print("---------------------带特殊参数的函数-----------------------")
def get_money_V4(cardNum,*args,**kwargs):
    print(cardNum)
    if len(cardNum) < 10 :
        print("卡号错了,再见!")
    print(args)
    print(kwargs)
    for item in args:
        print(item)

# get_money_V4("12345678900")
# print("---------------------------------------------------------")
# get_money_V4("12345678900",True,"123456",100)
# print("---------------------------------------------------------")
# get_money_V4("12345678900",True,"123456",name="小简",city="长沙")
# print("---------------------------------------------------------")
# res = get_money_V4("12345678900",True,"123456",name="小简",city="长沙")
# print(res)
print("---------------------------------------------------------")
get_money_V4("12345678900",emails="znsn",name="小简",city="长沙")

print("------------------------函数V5----------------------------")
def get_money_V5(cardNum,passwd="123456",count=1000):
    if len(cardNum) < 10:
        print("卡号错了,再见!")
        return cardNum      #遇到return就退出函数调用
    if len(passwd) != 6:
        print("密码长度出错,再见!")
        return
    if int(count) % 100 != 0:
        print("金额不为100的整数倍!")
    else:
        print("条件满足,准备吐钱...")
        return cardNum,count

carn,money = get_money_V5("123456789000",count=2000)
print("carn="+carn+",money="+str(money))

























