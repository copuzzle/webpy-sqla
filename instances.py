# -*- coding: utf-8 -*-
import web
import json
import time
import random
from model.dbmodel import *

#全局host 配置
host = web.ctx.get("homedomain", "http://wulei19881218.gicp.net:8080")
#host = "http://wulei19881218.gicp.net:8080"


#用户提交信息，注册
class Register():
    def GET(self):
        statuDict = {0: "注册成功", 1: "用户存在", 2: "验证码不存在", 10: "查询失败", 11: "系统错误"}
        statu = 0
        data = web.input()
        returnDict = {}
        invita_code = data.get("invita_code")
        phone_number = data.get("phone_number")
        verification_code = data.get("verification_code")
        password = data.get("password")
        #session = Session()
        session = web.ctx.orm()
        try:
            phone_record = session.query(Users).filter(Users.user_name == phone_number).first()
            is_verification_code_exist = session.query(UserCode).filter(UserCode.code_num == invita_code).first()
            if phone_record:
                statu = 1
                returnDict = {"code": statu, "ermsg": statuDict[statu]}
                return json.dumps(returnDict)
            elif not is_verification_code_exist:
                statu = 2
                returnDict = {"code": statu, "ermsg": statuDict[statu]}
                return json.dumps(returnDict)
            else:
                user = Users()
                user.user_name = phone_number
                user.password = password
                user.reg_time = int(time.time())
                session.add(user)
                session.commit()
                statu = 0
                returnDict = {"code": statu, "ermsg": statuDict[statu]}
                return json.dumps(returnDict)
        except Exception, e:
            #raise
            #return str(e)
            statu = 11
            returnDict = {"code": statu, "ermsg": statuDict[statu]}
            return json.dumps(returnDict)


if __name__ == "__main__":
    print get_n_random_number(8)
