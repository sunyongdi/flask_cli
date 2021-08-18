#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/12 11:02 上午
# software: PyCharm
"""
文件说明：
"""
from config.setting_globle import SettingGloble


class DefaultConfig(SettingGloble):
    """
    Flask 默认配置
    """
    DEBUG_MODEL_SWITCH = True
    SECRET_KEY = 'sunyongdi'  # 加密

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

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 容联云
    ACCID = '8a216da8762cb457017674f5bdc41dd3'
    ACCTOKEN = '9db6b1ab6c6e4312bf7efa1d41ca7da3'
    APPID = '8a216da87b52cabc017b533a39c1004e'

    ERROR_404_HELP = False

    # 日志
    LOGGING_LEVEL = 'DEBUG'
    import os
    BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
    LOGGING_FILE_DIR = '/Users/sunyongdi/Desktop/python/北大软件/flask学习/logs'
    LOGGING_FILE_MAX_BYTES = 300 * 1024 * 1024
    LOGGING_FILE_BACKUP = 10
