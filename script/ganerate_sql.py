#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/12 7:40 下午
# software: PyCharm
"""
文件说明：
数据表生成文件
"""

from framework import db
from app.v1.models.User import User


def initdb():
    db.create_all()
    print('数据库创建完成')


def dropdb():
    db.drop_all()
    print('清空数据库')


if __name__ == '__main__':
    dropdb()
    initdb()
