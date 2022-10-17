def filtering_integer_by_for(list_content):
    for item in list_content:
        if isinstance(item, int):
            result_list.append(item)
    return result_list


def filtering_integer_by_list_comprehensions(list_content):
    integer_list = [item for item in list_content if isinstance(item, int)]
    return integer_list


def filtering_integer_by_filter_and_lambda(list_content):
    result = list(filter(lambda x: isinstance(x, int), list_content))
    return result


if __name__ == '__main__':
    l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
    result_list = []
    print(filtering_integer_by_for(l))
    print(filtering_integer_by_list_comprehensions(l))
    print(filtering_integer_by_filter_and_lambda(l))
