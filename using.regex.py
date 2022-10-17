import re

text = """Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира, только у троих футболистов средний 
        показатель превышает 2 гола за игру. Эти 35 игроков представляют 14 футбольных сборных"""


def multiplied(matchobj):
    number = matchobj.group(0)
    multiplied_number = int(number) * 2
    string_number = str(multiplied_number)
    return string_number


final_text = re.sub(r'\b\d+\b', multiplied, text)
print(text)
print(final_text)
