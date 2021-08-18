#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/17 4:33 下午
# software: PyCharm
"""
文件说明：
"""
from ronglian_sms_sdk import SmsSDK
from random import randint
accId = '8a216da8762cb457017674f5bdc41dd3'
accToken = '9db6b1ab6c6e4312bf7efa1d41ca7da3'
appId = '8a216da87b52cabc017b533a39c1004e'

def send_message(mobile, code):
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    mobile = mobile
    datas = (code, '2')
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)

mobile = 18342960707
code = "{:0>6d}".format(randint(0, 9999))
send_message(mobile, code)
# send_message()
