"""
@Author:陈锐安
@Time:2021/12/24 0024 下午 3:36
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
list_my = []
print(type(list_my))

list_python30 = [0,1,2,3,4,5,6,7,8,9,"陈锐安"]

print(list_python30)

print(list_python30.index("陈锐安"))

list_python30.append("落魄的小测试")
list_python30.append(11)
print(list_python30)

list_python30.insert(0,"小猪猪")
print(list_python30)

new_list = ["荒年","henry","Null"]
list_python30.extend(new_list)
print(list_python30)

index = list_python30.index(0)
print(index)
list_python30[index] = "不要再长肉了"
print(list_python30)

print(list_python30.remove(11))
print(list_python30)
del  list_python30[0]
print(list_python30)

last_value = list_python30.pop()
print(list_python30)
print(last_value)

print(len(list_python30))
item = list_python30[len(list_python30)-1]
print(item)

result = '荒年' in list_python30
print(result)

result2 = "是包子呀呀呀呀" not in list_python30
print(result2)


print("11" in "1122222222223333333")