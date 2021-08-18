#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/18 9:59 下午
# software: PyCharm
"""
文件说明：
"""
from enum import Enum


class RespCode(Enum):
    """
    状态码常量类

    系统错误： 1000
    正常： 2000
    通用异常：3000
    数据异常： 4000
    Web异常： 5000
    App异常： 6000
    运维异常： 7000
    """
    INNER_ERROR = 1001
    PLEASE_TRY_LATER = 1002

    OK = 2000

    TOKEN_INVALID = 3001
    TOKEN_EXPIRED = 3002
    PARAM_LACK = 3003
    PARAM_WRONG_FORMAT = 3004
    UNAUTHORIZED = 3005
    POST_REPEAT = 3007
    REQUEST_METHOD_INVALID = 3008
    INVALID_PARAM = 3009
    NOT_SUPPORT = 3010
    NOT_FOUND_DATA = 3011
    INVALID_OPERATION = 3012

    DATA_ERROR = 4001
    NOT_FOUND_USER = 4004

    def desc(self):
        desc_dict = {
            RespCode.INNER_ERROR: '内部错误',
            RespCode.PLEASE_TRY_LATER: '操作失败，请稍后重试',

            RespCode.OK: "访问成功",

            RespCode.TOKEN_INVALID: '非法的token',
            RespCode.TOKEN_EXPIRED: 'token已失效',
            RespCode.PARAM_LACK: '缺失参数',
            RespCode.PARAM_WRONG_FORMAT: '参数格式不正确',
            RespCode.UNAUTHORIZED: '未授权',
            RespCode.POST_REPEAT: '重复提交',
            RespCode.REQUEST_METHOD_INVALID: '非法的请求方式',
            RespCode.INVALID_PARAM: '非法的请求参数',
            RespCode.NOT_SUPPORT: '不支持该操作',
            RespCode.NOT_FOUND_DATA: '找不到数据',
            RespCode.INVALID_OPERATION: '无效操作',

            RespCode.DATA_ERROR: '数据错误',

            RespCode.NOT_FOUND_USER: 'user_code 未知'
        }
        return desc_dict.get(self)
