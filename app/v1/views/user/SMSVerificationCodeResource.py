#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/18 7:32 下午
# software: PyCharm
"""
文件说明：
"""
from flask_restful import Resource
from flask import request, current_app
import random
from framework.constant.ConstantTime import SMS_VERIFICATION_CODE_EXPIRES
from framework.component.sms.send_sms import send_message


class SMSVerificationCodeResource(Resource):
    """
    服务器生成四位验证码，保存redis
    发送短信
    """
    def get(self, mobile):
        code = '{:0>4d}'.format(random.randint(0, 9999))
        current_app.redis_pool.setex('app:code:{}'.format(mobile), SMS_VERIFICATION_CODE_EXPIRES, code)
        send_message(mobile, code, SMS_VERIFICATION_CODE_EXPIRES)
        return {'monbile': mobile}
