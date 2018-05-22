from flask import Flask
from utils.settings import template_dir, static_dir
from app.user_views import user_blueprint
from utils.functions import init_ext
from app.house_views import house_blueprint


def creat_app(config):

    app = Flask(__name__, template_folder=template_dir,
                static_folder=static_dir)

    app.config.from_object(config)

    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
    app.register_blueprint(blueprint=house_blueprint, url_prefix='/house')

    init_ext(app)

    return app
