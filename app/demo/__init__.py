from flask import Blueprint
from flask_restful import Api

from app.demo.views.Login import Login
from app.demo.views.demo1 import Demo1
from app.demo.views.demo2 import Demo2
from app.demo.views.Register import Register
from app.demo.views.Index import Index
from app.demo.views.demo_redis import Demo_redis

api_blueprint = Blueprint('api', __name__)
api_blueprint_rest = Api(api_blueprint)

api_blueprint_rest.add_resource(Login, '/login')
api_blueprint_rest.add_resource(Demo1, '/demo1')
api_blueprint_rest.add_resource(Demo2, '/demo2')
api_blueprint_rest.add_resource(Register, '/register')
api_blueprint_rest.add_resource(Index, '/index')
api_blueprint_rest.add_resource(Demo_redis, '/demo_redis')
