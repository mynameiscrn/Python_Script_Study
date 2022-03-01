"""
@Author:陈锐安
@Time:2022/2/16 0016 下午 6:10
@Project:让工作变得轻松
@Address:广东省东莞市大朗镇巷头社区
"""
def login_check(username=None,password=None):
    if username != None and password != None:
        if username == 'python27' and password == 'lemonban':
            return {'code':0,'msg':'登录成功'}
        else:
            return {'code':1,'msg':"账号或密码不正确"}
    else:
        return {"code":1,"msg":"所有的参数不能为空"}