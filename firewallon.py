#!/usr/bin/python3
# -*- Adding Firewall on an IP Address -*-
"""
Created on Fri March 22 2024
@author: Okeke Morgan
"""
import os
import sys

if __name__ == '__main__':
    """
        Return:
            None
    """
    args = sys.argv
    if len(args) != 2:
        print("Usage: {} Filename targetHost")
        exit(1)
    ip_address = args[1]
    command = f"sudo iptables -A INPUT -s {ip_address} -j DROP"
    print(f" IP address {ip_address} is now protected from scanning and exploration. ")

