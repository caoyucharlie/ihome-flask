from flask import Flask
from utils.settings import template_dir, static_dir
from app.views import user_blueprint
from utils.functions import init_ext


def creat_app(config):

    app = Flask(__name__, template_folder=template_dir,
                static_folder=static_dir)

    app.config.from_object(config)

    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')

    init_ext(app)

    return app
