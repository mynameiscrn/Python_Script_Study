"""
@Author:陈锐安
@Time:2022/1/18 0018 上午 11:35
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
import requests
import json

# response = requests.post('http://httpbin.org/post')
# print(response.text)


payload = {
    "Overall":"良好",
    "Progress":"30%",
    "Problems":[
        {
            "No" : 1,
            "desc": "问题1...."
        },
        {
            "No" : 2,
            "desc": "问题2...."
        },
    ]
}
print(type(payload))
print(payload)
print(type(json.dumps(payload)))
print(json.dumps(payload))