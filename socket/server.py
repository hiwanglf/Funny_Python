#!/usr/bin/env python
import socket
import time
import os
# define HOST and PORT for server
HOST = '0.0.0.0'
PORT = 9999


def run_as_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        con, addr = server.accept()
        with con:
            # 将当前时间格式化成字符串
            # str_time = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime(int(time.time())))
            # print(str_time + " Connect By:", addr)
            pid = os.fork()
            if pid == 0:
                # 子进程用于写入发送消息
                while True:
                    con.sendall(b"Server: " + str.encode(input()))
            else:
                # 父进程接收消息
                while True:
                    data = con.recv(1024)
                    print("From Client: " + repr(data))


if __name__ == '__main__':
    run_as_server()
