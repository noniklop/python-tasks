import os


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
    tree = os.walk('C:/Users/Vladyslav_Melnychuk1/PycharmProjects')
    result_find = []
    find_content(".pyc")
    print("Count result: ", len(result_find))
