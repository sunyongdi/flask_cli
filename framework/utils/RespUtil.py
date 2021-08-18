#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/18 10:05 下午
# software: PyCharm
"""
文件说明：
"""

from framework.constant.RespCode import RespCode
from framework.vo.RespResult import RespResult

class RespUtil(object):
    # TODO 添加验证
    @staticmethod
    def ok(data=None) -> RespResult:
        return RespResult(RespCode.OK, {} if data is None else data).build()


    @staticmethod
    def unauthorized() -> RespResult:
        return RespResult(RespCode.UNAUTHORIZED, {}).build()

    @staticmethod
    def data_error(msg='') -> RespResult:
        return RespResult(RespCode.DATA_ERROR, msg).build()

    @staticmethod
    def not_found_data(msg='') -> RespResult:
        return RespResult(RespCode.NOT_FOUND_DATA, msg).build()