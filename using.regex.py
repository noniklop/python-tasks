import re


def multiplied(target_text):
    final_text = re.sub(r'\b\d+\b', lambda number: str(int(number.group()) * 2), target_text)

    return final_text


if __name__ == '__main__':
    text = """Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира, только у троих футболистов средний 
            показатель превышает 2 гола за игру. Эти 35 игроков представляют 14 футбольных сборных"""
    print(text)
    print(multiplied(text))
