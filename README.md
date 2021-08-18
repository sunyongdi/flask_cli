# 子系统API脚手架

## 版本

v 1.1.2

## 使用说明

* 该脚手架为子系统提供基础框架，以便业务快速开发
* 最新版本通过ssh://git@221.218.6.146:6022/api-framework获取

### 初始化
业务系统从git仓库中下载API框架后，需：
1. 重命名项目文件夹
2. 删除.git文件夹

### 目录结构
* app: 接口文件
    + doc：文档
* config：配置文件
* framework：基础框架功能
    + api: 接口
    + component：组件
    + constant：常量
    + context：上下文
    + decorator：装饰器
    + utils：工具
    + vo：视图对象
* script：脚本
* test：测试

### 文件说明
* app/blueprint.py：注册flask蓝图用
* config/setting_dev.py：开发环境配置
* config/setting_job.py：脚本执行环境配置
* config/setting_pro.py：生产环境配置
* config/setting_test.py：测试环境配置
* framework/api/AbstractApi.py：接口抽象类，所有接口都应该继承此类，按需要扩展此类
* framework/component/AbstractComponent.py：组件抽象类，所有组件都应该继承此类，按需要扩展此类
* framework/component/LogComponent.py：日志组件
* framework/constant/RequestMethod.py：请求方式常量
* framework/constant/RespCode.py：响应码常量
* framework/constant/SysConstant.py：系统常量
* framework/constant/Testing.py：测试相关常量
* framework/context/request_context_handlers.py：请求上下文处理器
* framework/util/ComplexEncoder.py：json序列化，对一些不支持序列化的数据进行处理
* framework/util/DatetimeUtil.py：日期工具类
* framework/util/DbUtil.py：数据库操作工具类
* framework/util/RespUtil.py：响应工具类
* framework/util/token_utils.py：token工具类
* framework/vo/RespResult.py：响应结果
* framework/\_\_init__.py: 在此文件中完成flask系统初始化配置、注册等功能
* test/test/AbstractTestCase.py：测试用例抽象类
* runserver.py：入口文件
* deploy.sh：部署并重启系统
* prod_gunicorn.conf.py：生产环境配置文件
* restart.sh：重启系统
* start.sh：启动系统
* stop.sh：停止系统

## 最佳实践

### 接口地址

```地址组成格式：http[s]:\\\\域名[ip]\业务应用名\版本\接口名?参数```

1. 有条件的，可以使用ssl加密
2. 尽量使用域名而不是ip
3. 版本从v1开始，依次v2、v3... 
4. 可以使用小版本号，列如v1.1，但不能超过1位小数

### APP

1. 接口创建在app目录中
2. 可以根据需求创建业务应用，一个应用一个目录
3. 在应用目录下的\_\_init__.py文件中定义蓝图及注册api路由
4. 接口定义在应用目录下的view目录下
5. 业务应用应根据需要分模块管理代码，比如component(组件)、constant(常量)、util(工具)、context(上下文)

###规范
1. 所有类以开头字母大写、驼峰方法命名，类所在的py文件与类名相同，一个py文件只能有一个类
2. 类属性、类方法、函数以小写、下划线分隔方式命名
3. 私有类属性以单下划线开头、私有方法已双下划线开头
4. 非类py文件，以小写、下划线分隔方式命令
5. 常用的常量应该尽量定义成枚举(Enum)类型

##返回响应数据格式
* 通过调用framework/utils/RespUtils.py中的方法返回固定格式数据，返回的数据格式为json，参考样式：
```
{
    code: 2000,
    msg: "访问成功"
    data: {
        username: "张三",
        role: "admin" 
    }
}
```
在framework/utils/constant/RespCode.py中定义了响应返回码


## 启动
1. 开发环境中可运行python runserver.py启动系统，runserver.py中定义了端口号
2. 在生产或者测试环境可以通过运行start.sh启动，但是需安装gunicorn

## 部署
1. 生产环境部署在/data/deploy/prod/子系统名/codes目录下
2. 测试环境部署在/data/deploy/test/子系统名/codes目录下

### 日志
- 在setting_globle中设置ENV为production， 默认development不启动  
- 添加日志
    ```python
    current_app.logger.info('info log')
    current_app.logger.warning('warning log') 
    try:
        pass
    except Exception as e:
        current_app.logger.exception(e)  

### redis
```python
current_app.redis_pool.set()
current_app.redis_pool.get()
current_app.redis_pool.setex()
```
### ！！！ 不需要用表单验证，状态保持使用token


# 电脑重启时  
- 启动redis
redis-server
  
- 启动mysql
mysql.server start
