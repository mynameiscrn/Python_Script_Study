"""
@Author:陈锐安
@Time:2022/1/27 0027 下午 1:39
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
from decimal import Decimal
Order_amount = 4
#总费率
Total_rate = 0.0038
Total = None
#易联票
YPL_rate = 0.0028
YPL = None
#代理商
Agent_rate = 0.0005
Agent = None
#总部
Headquarters_rate = 0.0005
Headquarters = None

Total = Order_amount * Total_rate
YPL = Order_amount * YPL_rate
Agent = Order_amount * Agent_rate
Headquarters = Order_amount * Headquarters_rate
print("总费率:"+str(Total)+",四舍五入后"+str(Decimal(str(Total)).quantize(Decimal('0.00'))))
print("易联票:"+str(YPL)+",四舍五入后"+str(Decimal(str(YPL)).quantize(Decimal('0.00'))))
print("代理商:"+str(Agent)+",四舍五入后"+str(Decimal(str(Agent)).quantize(Decimal('0.00'))))
print("总部:"+str(Headquarters)+",四舍五入后"+str(Decimal(str(Headquarters)).quantize(Decimal('0.00'))))

while Order_amount != 'ok':
    print('**************************这是下一轮的开始**************************')
    Order_amount = float(input("请输入订单的总额:"))
    Total = Order_amount * Total_rate
    YPL = Order_amount * YPL_rate
    Agent = Order_amount * Agent_rate
    Headquarters = Order_amount * Headquarters_rate
    print("总费率:" + str(Total) + ",四舍五入后:" + "{:.2f}".format(Total))
    print("易联票:" + str(YPL) + ",四舍五入后:" + "{:.2f}".format(YPL))
    print("代理商:" + str(Agent) + ",四舍五入后:" + "{:.2f}".format(Agent))
    print("总部:" + str(Headquarters) + ",四舍五入后:" + "{:.2f}".format(Headquarters))

