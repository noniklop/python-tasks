l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]


def filtering_integer_by_for():
    for item in l:
        if type(item) == int:
            print(item)


def filtering_integer_by_list_comprehensions():
    integer_list = [item for item in l if type(item) == int]
    return print(integer_list)


def filtering_integer_by_filter_and_lambda(list_content):
    result = list(filter(lambda x: type(x) == int, list_content))
    return print(result)


if __name__ == '__main__':
    filtering_integer_by_for()
    filtering_integer_by_list_comprehensions()
    filtering_integer_by_filter_and_lambda(l)
