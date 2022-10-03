number_bytes = int(input("Write bites: "))


def format_bytes(bytes):
    if bytes < 1024:
        print('{:.1f}'.format(bytes) + "B")
    if 1024 <= bytes < 1048576:
        bytes /= 1024
        print('{:.1f}'.format(bytes) + "Kb")
    if 1048576 <= bytes < 1073741824:
        bytes /= 1048576
        print('{:.1f}'.format(bytes) + "Mb")
    if bytes >= 1073741824:
        bytes /= 1073741824
        print('{:.1f}'.format(bytes) + "Gb")

if __name__ == '__main__':
    format_bytes(number_bytes)