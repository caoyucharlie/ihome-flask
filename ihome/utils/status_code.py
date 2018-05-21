

OK = 200

SUCCESS = {'code': 200, 'msg': '请求成功'}

PARAMS_ERROR = {'code': 901, 'msg': '参数错误'}

DATABASE_ERROR = {'code': 900, 'msg': '数据库访问失败'}


# 用户模块
USER_REGISTER_PARAMS_ERROR = {'code': 1000, 'msg': '注册信息错误'}

USER_REGISTER_MOBILE_ERROR = {'code': 1001, 'msg': '注册手机号码不符合规则'}

USER_REGISTER_MOBILE_IS_EXSITS = {'code': 1002, 'msg': '手机号码已注册'}

USER_REGISTER_PASSWORD_IS_ERROR = {'code': 1003, 'msg': '注册密码两次不一致'}

USER_LOGIN_IS_NOT_EXSITS = {'code': 1004, 'msg': '用户不存在'}
USER_LOGIN_PASSWORD_IS_ERROR = {'code': '1005', 'msg': '用户登录密码错误'}

USER_UPLOAD_IMAGE_IS_ERROR = {'code': '1006', 'msg': '上传图片不符合标准'}