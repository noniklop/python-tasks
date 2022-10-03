def sum_multiplies():
    result = 0
    for item in range (1, 100000001):
        if item % 3 == 0 or item % 5 == 0:
            result += item
    print(result)


if __name__ == "__main__":
    sum_multiplies()