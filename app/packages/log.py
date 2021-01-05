"""
@Time : 2021/01/05 16:25
@Email : nrhyhy@163.com
@Author : NRH
@File : log.py
"""
import logging

from flask.logging import default_handler

from config import Config


def setup_log(app):
    """
    更改flask默认log
    :param app: flask app
    :return:
    """
    # 移除默认handler
    app.logger.removeHandler(default_handler)

    flask_logger = logging.getLogger()
    flask_logger.setLevel(Config.LOG_LEVEL)

    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
    stream_handler.setFormatter(formatter)

    for logger in (
            # 这里还可以添加其它模块，如elasticsearch/sqlalchemy
            app.logger,  # 打印日志方式：current_app.logger.warning('--')
            logging.getLogger('werkzeug'),
            logging.getLogger('gevent'),
            logging.getLogger('sqlalchemy')
    ):
        logger.addHandler(stream_handler)
