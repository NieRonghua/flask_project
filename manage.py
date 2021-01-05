"""
@Time : 2021/01/05 16:08
@Email : nrhyhy@163.com
@Author : NRH
@File : manage.py
"""
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()

from multiprocessing import cpu_count, Process

from app import create_app

app = create_app()


def run(multi_process):
    """
    false: 单进程+协程, true: 多进程+协程
    :param multi_process: bool
    :return:
    """
    if not multi_process:
        WSGIServer(('0.0.0.0', 8080), app).serve_forever()
    else:
        multi_server = WSGIServer(('0.0.0.0', 8080), app)
        multi_server.start()

        def server_forever():
            multi_server.start_accepting()
            multi_server._stop_event.wait()

        for i in range(cpu_count()):
            p = Process(target=server_forever)
            p.start()


if __name__ == '__main__':
    run(True)