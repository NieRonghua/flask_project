"""
@Time : 2021/01/05 16:22
@Email : nrhyhy@163.com
@Author : NRH
@File : error_handler.py
"""


def init_error_handler(app):
    """
    自定义响应状态码错误捕捉
    :param app: flask app
    :return:
    """

    @app.errorhandler(404)
    def error_404(error):
        return f'当前响应404，错误提示: {error}'

    @app.errorhandler(405)
    def error_405(error):
        return f'当前响应405，错误提示: {error}'