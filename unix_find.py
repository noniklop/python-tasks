import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", type=str)
args = parser.parse_args()

result_find = []
tree = os.walk('C:/Users/Vladyslav_Melnychuk1/PycharmProjects/')


def find_content(name_content):
    for i in tree:
        for x in i:
            if type(x) == list:
                for y in x:
                    if name_content in y:
                        print(y)
                        result_find.append(y)


if __name__ == "__main__":
    find_content(".pyc")
    print("Count result: ", len(result_find))
