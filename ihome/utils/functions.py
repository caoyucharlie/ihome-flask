from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def get_db_uri(DATABASE):
    user = DATABASE.get('USER')
    password = DATABASE.get('PASSWORD')
    host = DATABASE.get('HOST')
    port = DATABASE.get('PORT')
    name = DATABASE.get('NAME')
    db = DATABASE.get('DB')
    driver = DATABASE.get('DRIVER')

    return '{}+{}://{}:{}@{}:{}/{}'.format(db, driver,
                                           user, password,
                                           host, port, name)


def init_ext(app):
    db.init_app(app=app)