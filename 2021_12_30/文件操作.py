"""
@Author:陈锐安
@Time:2022/1/11 0011 上午 9:19
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
#fs = open("py31.txt")
fs = open(r"D:\Python_Script\2021_12_30\py31.txt","a",encoding="utf-8")
#一下子获取文本的全部内容
# s = fs.read()
# print(s)
# s1 = fs.readline()
# print(s1)
# s2 = fs.readline()
# print(s2)
# s3 = fs.readline()
# print(s3)

# fs.write("大家好,hello,World! 111111\n")  #w模式  文件覆盖写入
# fs.write("py30,year!!!!!!!")

fs = open("new_file1.txt","a",encoding="utf-8")
# fs.write("我是新的文件!hello python!")
fs.close()

with open("new_file2.txt","a",encoding="utf-8") as fs:
    fs.write("我是鼎鼎大名的陈同学")

