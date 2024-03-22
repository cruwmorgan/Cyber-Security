#!/usr/bin/python3
# -*- Changing Mac Address of my Linux -*-
"""
Created on Fri March 22 2024
@author: Okeke Morgan
"""
import subprocess
import sys

if __name__ == '__main__':
    """
        Return:
            None
    """
    args = sys.argv
    if len(args) != 3:
        print("Usage: {} Interface NewMacAddress".format(args[0]))
        exit(1)
    interface = args[1]
    new_mac = args[2]

    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call("sudo ifconfig " + interface + " down ", shell=True)
    subprocess.call("sudo ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("sudo ifconfig " + interface + " up ", shell=True)
    subprocess.call("ifconfig " + interface + "", shell=True)
