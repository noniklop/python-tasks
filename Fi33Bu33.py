for item in range(1, 101):
    if item % 3 == 0 and item % 5 == 0:
        item = "FizzBuzz"
        print(item)
        continue
    if item % 3 == 0:
        item = "Fizz"
        print(item)
        continue
    if item % 5 == 0:
        item = "Buzz"
        print(item)
        continue
    print(item)