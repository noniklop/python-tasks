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


def check_valid_ip_re(ip):
    bytes_ip = ip.split(".")
    check_ip = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip)
    for ip_byte in bytes_ip:
        if 0 < int(ip_byte) > 255 or check_ip is None:
            return print("Invalid ip: ", ip)
        if len(bytes_ip) != 4:
            return print("Invalid ip: ", ip)
    print("Valid ip")


if __name__ == "__main__":
    check_valid_ip_socket(input_ip)
    check_valid_ip_re(input_ip)
