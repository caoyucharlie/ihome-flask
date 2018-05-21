
import re
import os
from flask import Blueprint, render_template, request, jsonify, session
from app.models import db, User
from utils import status_code
from utils.settings import UPLOAD_DIRS

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/create')
def create():
    db.create_all()
    return '创建成功'


@user_blueprint.route('/register/', methods=['GET'])
def register():
    return render_template('register.html')


@user_blueprint.route('/register/', methods=['POST'])
def user_register():
    '''
    注册请求api
    '''
    register_dict = request.form
    mobile = register_dict.get('mobile')
    password = register_dict.get('password')
    password2 = register_dict.get('password2')
    # 只要有参数为空，返回false
    if not all([mobile, password, password2]):

        return jsonify(status_code.USER_REGISTER_PARAMS_ERROR)
    if not re.match(r'^1[345678]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_ERROR)

    if User.query.filter(User.phone == mobile).count():
        return jsonify(status_code.USER_REGISTER_MOBILE_IS_EXSITS)

    if password != password2:
        return jsonify(status_code.USER_REGISTER_PASSWORD_IS_ERROR)

    user = User()
    user.phone = mobile
    user.name = mobile
    user.password = password
    try:
        user.add_update()
        return jsonify(status_code.SUCCESS)
    except Exception as e:
        return jsonify(status_code.DATABASE_ERROR)


@user_blueprint.route('/login/', methods=['GET'])
def login():
    '''
    登录页面
    :return:
    '''
    return render_template('login.html')
'''
POST登录api
'''


@user_blueprint.route('/login/', methods=['POST'])
def user_login():

    user_dict = request.form

    mobile = user_dict.get('mobile')
    password = user_dict.get('password')

    if not all([mobile, password]):

        return jsonify(status_code.PARAMS_ERROR)

    if not re.match(r'^1[345678]\d{9}$', mobile):
        return jsonify(status_code.USER_REGISTER_MOBILE_ERROR)

    user = User.query.filter(User.phone == mobile).first()
    if user:
        if user.check_pwd(password):
            session['user_id'] = user.id
            return jsonify(status_code.SUCCESS)
        else:
            return jsonify(status_code.USER_LOGIN_PASSWORD_IS_ERROR)
    else:
        return jsonify(status_code.USER_LOGIN_IS_NOT_EXSITS)


@user_blueprint.route('/my/', methods=['GET'])
def my():
    return render_template('my.html')


@user_blueprint.route('/user/', methods=['GET'])
def get_user_profile():

    user_id = session['user_id']
    user = User.query.get(user_id)

    return jsonify(user=user.to_basic_dict(), code='200')


@user_blueprint.route('/profile/', methods=['GET'])
def profile():
    return render_template('profile.html')


# @user_blueprint.route('/profile/', methods=['PUT'])
# def profile():
#     file_dicts = request.files


@user_blueprint.route('/user/', methods=['PUT'])
def user_profile():

    file_dict = request.files
    if 'avatar' in file_dict:
        f1 = request.files['avatar']

        if not re.match(r'^image/*$', f1.mimetype):
            return jsonify(status_code.USER_UPLOAD_IMAGE_IS_ERROR)

        url = os.path.join(UPLOAD_DIRS, f1.filename)
        f1.save(url)

        user = User.query.filter(User.id == session['user_id'])

        image_url = os.path.join('/static/upload', f1.filename)
        user.avatar = image_url
        try:
            user.add_update()
            return jsonify(code=status_code.OK, url=image_url)
        except Exception as e:
            return jsonify(status_code.DATABASE_ERROR)

