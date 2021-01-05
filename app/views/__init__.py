"""
@Time : 2021/01/05 15:52
@Email : nrhyhy@163.com
@Author : NRH
@File : __init__.py.py
"""
from app.views.api_test import test


def register_blue_print(app):
    """
    注册蓝图
    :param app: flask app
    :return:
    """

    # graph
    app.register_blueprint(test)