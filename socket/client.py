import socket
import time
import os
import threading
# define Marcro
HOST = '192.168.246.135'
PORT = 9999


def input_msg(con):
    while True:
        con.sendall(str.encode(input()))


def get_msg(con):
    while True:
        data = con.recv(1024)
        print("From Server: " + repr(data))


def run_as_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        # 如果是Linux/UNIX系统，使用多进程
        if os.name == 'posix':
            pid = os.fork()
            if pid == 0:
                while True:
                    client.sendall(str.encode(input()))
            else:
                while True:
                    # str_time = time.strftime("[%Y-%m-%d %H:%M:%S]", time.localtime(int(time.time())))
                    data = client.recv(1024)
                    print("From Server: " + repr(data))
        else:
            t1 = threading.Thread(target=input_msg, args=(client,))
            t2 = threading.Thread(target=get_msg, args=(client,))
            t1.start()
            t2.start()
            t1.join()
            t2.join()


if __name__ == '__main__':
    run_as_client()
