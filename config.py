"""
@Time : 2021/01/05 16:09
@Email : nrhyhy@163.com
@Author : NRH
@File : config.py
"""
import logging
import os


class Config(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    MYSQL_IP = os.environ.get("MYSQL_IP", 'lbcr-m.dbsit.sfcloud.local')
    MYSQL_PORT = os.environ.get("MYSQL_PORT", 3306)
    MYSQL_USER = os.environ.get("MYSQL_USER", 'lbcr')
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", '0fc91ac6')
    MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE", 'lbcr')

    SQLALCHEMY_DATABASE_URI = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_IP}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 自动追踪对象的修改并且发送信号
    SQLALCHEMY_RECORD_QUERIES = True  # 开启使get_debug_queries()生效
    SQLALCHEMY_ECHO = False  # 查询是否显示原生SQL语句
    SQLALCHEMY_POOL_RECYCLE = 299  # 自动回收连接的秒数，默认2h
    SQLALCHEMY_POOL_TIMEOUT = 20  # 数据库连接池的超时时间，默认是10s

    LOG_LEVEL = logging.INFO

    @staticmethod
    def init_app(app):
        pass
