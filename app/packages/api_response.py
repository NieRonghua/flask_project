"""
@Time : 2021/01/05 16:35
@Email : nrhyhy@163.com
@Author : NRH
@File : api_response.py
"""
from flask import jsonify

from app.models import Response


def res(code, data=None, message=''):
    """
    返回响应信息
    :param code: 状态码
    :param data: 响应数据
    :param message: 提示信息
    :return:
    """
    if Response.is_succeed(code):
        message = Response.res_map[Response.SUCCESS]
    else:
        if not message:
            message = Response.get_msg_from_code(code)

    return jsonify({
        'status_code': code,
        'message': message,
        'data': data

    })
