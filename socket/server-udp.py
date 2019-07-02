#!/usr/bin/env python

import socket
import threading

HOST = '0.0.0.0'
PORT = 9998
global ADDR


def udp_receive(con):
    while True:
        data, addr = con.recvfrom(1024)
        print(data)


def udp_send(con, addr):
    while True:
        con.sendto(str.encode(input()), addr)


def run_udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
        server.bind((HOST, PORT))
        data, addr = server.recvfrom(1024)
        t_rcv = threading.Thread(target=udp_receive, args=(server,))
        t_send = threading.Thread(target=udp_send, args=(server, addr))

        t_rcv.start()
        t_send.start()

        t_rcv.join()
        t_send.join()


if __name__ == '__main__':
    run_udp_server()

