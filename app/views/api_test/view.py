"""
@Time : 2021/01/05 16:32
@Email : nrhyhy@163.com
@Author : NRH
@File : view.py
"""
from flask import current_app

from app.models import Response
from app.packages.api_response import res
from app.views.api_test import test


@test.route('/', methods=['get'])
def test():
    current_app.logger.warning('hello world')

    return res(code=Response.SUCCESS, data='hello world!')
