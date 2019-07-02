#!/usr/bin/env python

import socket

HOST = '192.168.246.135'
PORT = 9998

def run_udp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        while True:
            client.sendto(str.encode(input()), (HOST, PORT))
            data = client.recv(1024).decode('utf-8')
            print(data)


if __name__ == '__main__':
    run_udp_client()
