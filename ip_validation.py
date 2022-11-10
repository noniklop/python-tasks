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
    check_ip = re.match(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", ip)
    if check_ip is not None:
        return True
    else:
        return False


if __name__ == "__main__":
    target_ip = '192.168.0.1'
    print("Status IP: ", check_valid_ip_socket(target_ip))
    # assert target_ip, check_valid_ip_re(target_ip)

    assert check_valid_ip_re('') is False
    assert check_valid_ip_re('192.168.0.1') is True
    assert check_valid_ip_re('0.0.0.1') is True
    assert check_valid_ip_re('10.100.500.32') is False
    assert check_valid_ip_re('700') is False
    assert check_valid_ip_re('127.0.0.1') is True
