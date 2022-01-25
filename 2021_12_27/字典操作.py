"""
@Author:陈锐安
@Time:2021/12/29 0029 下午 1:45
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
num_list = [120,250,11,44,77,45,22,390]
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)


print(num_list[::-1])
num_list.reverse()
print(num_list)

my_tuple = ()
my_tuple2 = (18,22,33,45,60,70)
print(my_tuple2[2])
my_tuple3 = ("hello",)
print(my_tuple3)
print(type(my_tuple3))

dog_info = { "name":"存钱罐","sex":"公","age":"3个月","type":"串疮","owner":"陈多多"}
my_dict = {}
print(dog_info)
print(dog_info["age"])
print(dog_info.get("age"))
print(dog_info.get("parent"))

dog_info["age"] = "3个半月"
print(dog_info)

dog_info["father"] = "金毛"
print(dog_info)
print(type(dog_info))
keys = dog_info.keys()
print(keys)
all_keys = list(keys)
print(all_keys)