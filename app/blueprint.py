from app.demo import api_blueprint

def register(app):
    """
    在这里注册蓝图
    """

    app.register_blueprint(api_blueprint, url_prefix='/api')