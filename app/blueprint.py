from app.v1 import v1_blueprint
from app.v2 import v2_blueprint
from app.v3 import v3_blueprint

def register(app):
    """
    在这里注册蓝图
    """
    app.register_blueprint(v1_blueprint, url_prefix='/v1')
    app.register_blueprint(v2_blueprint, url_prefix='/v2')
    app.register_blueprint(v3_blueprint, url_prefix='/v3')