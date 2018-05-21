
import os
from utils.functions import get_db_uri

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

template_dir = os.path.join(BASE_DIR, 'templates')
static_dir = os.path.join(BASE_DIR, 'static')

DATABASE = {
    'USER': 'root',
    'PASSWORD': 'jy2190883',
    'HOST': '47.106.144.34',
    'PORT': '3306',
    'DB': 'mysql',
    'DRIVER': 'pymysql',
    'NAME': 'ihome'
}

SQLACHEMY_DATABASE_URI = get_db_uri(DATABASE)

UPLOAD_DIRS = os.path.join(os.path.join(BASE_DIR, 'static'), 'upload')
