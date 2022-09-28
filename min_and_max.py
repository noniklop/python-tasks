numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
list_without_words = []
for item in numbers:
    try:
        list_without_words.append(int(item))
    except Exception as e:
        print("Error: ",e)
print("Max value: ", max(list_without_words))
print("Min value: ", min(list_without_words))