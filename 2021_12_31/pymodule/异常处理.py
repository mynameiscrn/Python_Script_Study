"""
@Author:陈锐安
@Time:2022/1/11 0011 上午 11:15
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
# dicta = {"name":"111"}
# print(dicta["key"])
try:
    fs = open(r"D:\Python_Script\2021_12_31\pymodule\123.txt",'r',encoding='utf-8')
    fs.write("写入成功")
except:
    print("代码出错了")
    # raise
else:
    print("恭喜我已经进入了else代码块~")
finally:
    print("hahaha不管你执行成功与否都会执行到我这里")
    try:
        fs.close()
    except:
        pass
print("okkkkk已经走到我这里了**&*&*&*&")