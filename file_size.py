def format_bytes(bytes):
    if 0 <= bytes < 1024:
        print('{:.1f}'.format(bytes) + "B")
    elif 1024 <= bytes < 1048576:
        bytes /= 1024
        print('{:.1f}'.format(bytes) + "Kb")
    elif 1048576 <= bytes < 1073741824:
        bytes /= 1048576
        print('{:.1f}'.format(bytes) + "Mb")
    elif bytes >= 1073741824:
        bytes /= 1073741824
        print('{:.1f}'.format(bytes) + "Gb")
    else:
        print("Error")

if __name__ == '__main__':
    number_bytes = int(input("Write bites: "))
    format_bytes(number_bytes)