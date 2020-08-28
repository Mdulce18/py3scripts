# Script for copy files to remote servers by scp
# ip.txt file necessary

import os
import time


def readtxt(file_name):
    with open(file_name, "r") as file:
        ip_list = file.read().splitlines()
        return ip_list


def copyfile(list):
    for ip in list:
        try:
            print(ip)
            os.system(f'scp -P <fileToCopyPath> remoteuser@{ip}:/<patInRemoteServer>/')
            print('---------------------')
            time.sleep(2)
        except KeyboardInterrupt:
            print("\nStopped by user")
            break


def main():
    ips = readtxt("ips.txt")
    copyfile(ips)


main()
