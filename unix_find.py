import os
import argparse

parser = argparse.ArgumentParser()


parser.add_argument('-t', '--target', type=str, help='Write what you want to find')
parser.add_argument('-p', '--place', type=str, help='Where find your target file')

args = parser.parse_args()


def find_content(name_content):
    for way in tree:
        for item in way:
            if isinstance(item, list):
                for file_name in item:
                    if name_content in file_name:
                        print("Founded file: ", file_name)
                        print("Way to file: ", way[0] + "\n")
                        result_find.append(file_name)


if __name__ == "__main__":
    tree = os.walk(args.place)
    result_find = []
    find_content(args.target)
    print("Count result: ", len(result_find))
