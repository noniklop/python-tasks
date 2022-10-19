import string


def count_letters(target_text):
    all_symbols = []
    same_symbols = []
    count_symbols = {}

    for item in target_text.lower():
        if item.isalpha() is True:
            all_symbols.append(item)

    for letter in string.ascii_letters:
        for symbol in all_symbols:
            if letter == symbol:
                same_symbols.append(symbol)
        if len(same_symbols) == 0:
            continue
        letter = same_symbols[0]
        count = len(same_symbols)
        count_symbols[letter] = count

        same_symbols.clear()

    return count_symbols


if __name__ == '__main__':
    text = """Python is an interpreted high-level programming language for general-purpose programming. Created by Guido
           van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability,
           notably using significant whitespace. It provides constructs that enable clear programming on both small and
           large scales. In July 2018, the creator Guido Rossum stepped down as the leader in the language community
           after 30 years. Python features a dynamic type system and automatic memory management. It supports multiple
           programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and
           comprehensive standard library. Python interpreters are available for many operating systems. CPython,
           the reference implementation of Python, is open source software and has a community-based development model,
           as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python
           Software Foundation. Привет из Харькова! """

    most_letter = max(count_letters(text), key=count_letters(text).get)

    all_values = count_letters(text).values()
    count_most_letter = max(all_values)

    print("Letter: " + most_letter)
    print("Count: ", count_most_letter)
