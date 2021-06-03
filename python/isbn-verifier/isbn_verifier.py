from typing import Counter


def is_valid(isbn):
    counter = 10
    sum = 0
    try:
        for char in isbn:
            if char == 'X' and counter != 1:
                return False
            if char == 'X':
                sum += 10*counter
                counter -= 1
            elif char == "-":
                continue
            else:
                sum += counter*int(char)
                counter -= 1
    except ValueError:
        return False

    if counter != 0:
        return False

    return sum%11 == 0
