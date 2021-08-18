#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# author:SunYondDi
# contact: 914767648@qq.com
# datetime:2021/8/8 12:32 下午
# software: PyCharm
"""
文件说明：框架
"""
from flask import Flask


def create_flask_app(config, enable_config_file=False):
    """
    创建Flask应用
    :param config: 配置信息对象
    :param enable_config_file: 是否允许环境中的配置文件覆盖已加载的配置信息
    :return: FLASK应用
    """
    app = Flask(__name__)
    app.config.from_object(config)
    if enable_config_file:
        from utils import constants
        app.config.from_envvar(constants.GLOBAL_SETTING_ENV_NAME, silent=True)

    return app


def create_app(config, enable_config_file=False):
    """
    创建应用
    :param config: 配置信息对象
    :param enable_config_file: 是否允许环境中的配置文件覆盖已加载的配置信息
    :return: FLASK应用
    """
    app = create_flask_app(config, enable_config_file)

    # Mysql数据连接初始化
    from app.demo.models import db
    db.init_app(app)

    # redis
    import redis
    pool = redis.ConnectionPool(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'], decode_responses=True)
    app.redis_pool = redis.Redis(connection_pool=pool)

    # 添加请求钩子
    from hooks.g_methods import get_name, validate_token
    app.before_request(get_name)  # 注意不要加()
    app.before_request(validate_token)  # 注意不要加()

    # 注册蓝图
    from app import blueprint
    blueprint.register(app)

    #
    # logging_manage = LoginManager()
    # logging_manage.init_app(app)

    # 配置
    # import os
    # from config.setting_logging import setting_logging
    # logs_path = os.path.join(os.path.abspath(os.path.dirname(app.root_path)), 'logs')
    # print('logs_path', logs_path)
    # if not os.path.exists(logs_path):
    #     os.makedirs(logs_path)
    #
    # setting_logging(app, logs_path)

    # 配置日志
    import os
    from config.setting_logging import setup_log
    logs_path = os.path.join(os.path.abspath(os.path.dirname(app.root_path)), 'logs')
    if app.config['ENV'] != 'development':
        setup_log(logs_path)

    return app
