l = [1, [], 2, [-19, 700, 0, [90, 33, [18, 77, [0,], -2], 11, 16], -100]]
all_content = []


def average(target_list):
    sum_list = sum(target_list)
    average_from_list = sum_list / len(target_list)
    return average_from_list


def all_content_in_one_list(list_content):
    for item in list_content:
        if type(item) == int:
            all_content.append(item)
        if type(item) == list:
            all_content_in_one_list(item)


def stat_value(list_content):
    print("Minimal value", min(list_content))
    print("Maximum value", max(list_content))
    print("Average value", '{:.2f}'.format(average(list_content)))


if __name__ == '__main__':
    all_content_in_one_list(l)
    stat_value(all_content)
