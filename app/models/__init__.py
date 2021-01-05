"""
@Time : 2021/01/05 15:52
@Email : nrhyhy@163.com
@Author : NRH
@File : __init__.py.py
"""


class Response(object):
    """
    自定义响应状态码code和提示信息message
    """
    def __init__(self):
        pass

    SUCCESS = 0
    PARAMS_REQUIRED = 4001
    PARAMS_TYPE_ERROR = 4002

    res_map = {
        SUCCESS: 'API请求成功',
        PARAMS_REQUIRED: '请求缺少参数',
        PARAMS_TYPE_ERROR: '参数类型错误'
    }

    @classmethod
    def is_succeed(cls, code):
        return True if code == cls.SUCCESS else False

    @classmethod
    def get_msg_from_code(cls, code):
        msg = cls.res_map.get(code, '')
        return msg
