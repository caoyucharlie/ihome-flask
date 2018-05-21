### 爱租客接口文档
### 用户模块

 -[登录接口](docs/user/user_login)

### 登录接口
### request请求
    POST/user/login/


### params参数:
    mobile str 电话号码
    password str 密码

### response响应

### 失败响应1:
    {
        'code': 1004,
        'msg': '用户不存在'
    }

### 失败响应2：
    {
    'code': '1005',
    'msg': '用户登录密码错误'
    }