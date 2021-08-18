#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/12 11:02 上午
# software: PyCharm
"""
文件说明：
"""


class DefaultConfig(object):
    """
    Flask 默认配置
    """
    SECRET_KEY = 'sunyongdi' # 加密

    WTF_CSRF_ENABLED = False
    WTF_I8N_ENABLED = False

    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@127.0.0.1/sparrow"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Zx123456@121.196.171.126:3306/sparrow" # 服务器
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@127.0.0.1:3306/tt_news"  # 本地
    # 主从复制使用
    # SQLALCHEMY_BINDS = {
    #     Testing.TEST_DB: "mysql+pymysql://root:Zx123456@121.196.171.126:3306/bokeyuan",
    # }
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        'echo_pool': True,
        'pool_size': 50,
        'max_overflow': 100,
        'pool_recycle': 30
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 追踪数据的修改信号
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
