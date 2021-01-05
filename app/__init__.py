"""
@Time : 2021/01/05 15:51
@Email : nrhyhy@163.com
@Author : NRH
@File : __init__.py.py
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.packages.error_handler import init_error_handler
from app.packages.log import setup_log
from app.views import register_blue_print
from config import Config

config = Config()
db = SQLAlchemy()


def create_app():
    """
    实例化 flask app
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)

    init_error_handler(app)
    db.init_app(app)
    setup_log(app)

    register_blue_print(app)

    return app
