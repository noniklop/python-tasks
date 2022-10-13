import socket
import re


def check_valid_ip_socket(ip):
    try:
        socket.inet_aton(ip)
        status_ip = True
    except socket.error:
        status_ip = False
    return status_ip


def check_valid_ip_re(ip):
    check_ip = re.match(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", ip)
    if check_ip is not None:
        print("Correct IP: ", check_ip.group(0))
    else:
        print("Invalid IP")


if __name__ == "__main__":
    input_ip = input("Insert your ip: ")
    print("Status IP: ", check_valid_ip_socket(input_ip))
    check_valid_ip_re(input_ip)
