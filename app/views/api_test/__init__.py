"""
@Time : 2021/01/05 16:31
@Email : nrhyhy@163.com
@Author : NRH
@File : __init__.py.py
"""
# 定义蓝图
from flask import Blueprint

test = Blueprint('test', __name__)

from . import view
