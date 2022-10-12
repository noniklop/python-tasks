numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
list_without_words = []


def min_and_max_value(list_numbers):
    for item in list_numbers:
        try:
            list_without_words.append(int(item))
        except (ValueError, TypeError) as e:
            print("Error: ", e)
    print("Max value: ", max(list_without_words))
    print("Min value: ", min(list_without_words))


if __name__ == '__main__':
    min_and_max_value(numbers)
