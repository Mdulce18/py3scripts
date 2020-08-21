#need ips file to select servers

import os


def readtxtandrun(file_name):
    with open(file_name, "r") as file:
        for line in file:
            ip_server = line.strip()
            os.system(f'scp -P <port> /<pathfile>/<file> root@{ip_server}:/root/')


readtxtandrun("ips.txt")
