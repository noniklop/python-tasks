def fizz_buzz():
    for item in range(1, 101):
        if item % 15 == 0:
            item = "FizzBuzz"
            print(item)
        elif item % 3 == 0:
            item = "Fizz"
            print(item)
        elif item % 5 == 0:
            item = "Buzz"
            print(item)
        else:
            print(item)


if __name__ == "__main__":
    fizz_buzz()
