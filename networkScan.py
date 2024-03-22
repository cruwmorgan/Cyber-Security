#!/usr/bin/python3
# -*- Network Port Scanning -*-
"""
Created on Fri March 22 2024
@author: Okeke Morgan
"""
import socket
import sys


def port_scan(target_host, target_port):
    """
        Args:
            target_host: string
            target_port: Array containing ports

        Return:
            None
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, target_port))
        if result == 0:
            print(f"Port {target_port} is open")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {target_port}: {e}")

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print("Usage: {} targetHost".format(args[0]))
        sys.exit(1)
    target_host = args[1]
    target_ports = [21, 22, 25, 80, 443, 8080] 

    for port in target_ports:
        port_scan(target_host, port)
