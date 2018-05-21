from utils.settings import SQLACHEMY_DATABASE_URI
import redis


class Config:

    SQLALCHEMY_DATABASE_URI = SQLACHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'secret_key'

    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis(host='47.106.144.34', port=6379)
    SESSION_KEY_PREFIX = 's_aj_'
