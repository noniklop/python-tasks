import socket
import re

input_ip = input("Insert your ip: ")


def check_valid_ip_socket(ip):
    try:
        socket.inet_aton(ip)
        status_ip = True
    except socket.error:
        status_ip = False
    return print("Status IP: ", status_ip)

def check_valid_ip_re(ip)


check_valid_ip_socket(input_ip)
