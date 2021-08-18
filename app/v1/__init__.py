from flask import Blueprint
from flask_restful import Api

#+++++++++++++++++++++导入视图+++++++++++++++++++++++++++
from app.v1.views.v1_demo import V1_demo
from app.v1.views.user.UserAuthentication import UserAuthentication
from app.v1.views.user.SMSVerificationCodeResource import SMSVerificationCodeResource
from app.v1.views.user.Login import Login
#+++++++++++++++++++++导入视图+++++++++++++++++++++++++++


v1_blueprint = Blueprint('v1', __name__)
v1_blueprint_rest = Api(v1_blueprint)



#+++++++++++++++++++++注册路由+++++++++++++++++++++++++++
v1_blueprint_rest.add_resource(V1_demo, '/demo')
v1_blueprint_rest.add_resource(UserAuthentication, '/user_authentication')
v1_blueprint_rest.add_resource(SMSVerificationCodeResource, '/sms_verification_code_resource/<mobile>')
v1_blueprint_rest.add_resource(Login, '/login')
#+++++++++++++++++++++注册路由+++++++++++++++++++++++++++