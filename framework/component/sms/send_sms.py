#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/17 5:34 下午
# software: PyCharm
"""
文件说明：
"""
from ronglian_sms_sdk import SmsSDK
from random import randint
from config.setting_dev import DefaultConfig


def send_message(mobile, code, etime):
    # TODO 使用celery 解阻塞
    sdk = SmsSDK(DefaultConfig.ACCID, DefaultConfig.ACCTOKEN, DefaultConfig.APPID)
    tid = '1'  # 短信模版
    mobile = mobile
    datas = (code, etime)
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)


# mobile = 18342960707
# code = "{:0>6d}".format(randint(0, 9999))
# send_message(mobile, code)
