#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/18 9:52 下午
# software: PyCharm
"""
文件说明：
"""
from framework.constant.RespCode import RespCode


class RespResult(object):
    def __init__(self, resp_code: RespCode, result: object):
        self._respcode = resp_code
        self._result = result

    def build(self):
        return {
            'code': self._respcode.value,
            'msg': self._respcode.desc(),
            'result': self._result
        }
