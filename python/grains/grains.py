def square(number):
    if not isinstance(number, int):
        raise ValueError('number must be an integer')
    if number < 1:
        raise ValueError('number must be greater than 0')
    if number > 64:
        raise ValueError('number must be less than 65')

    return 2**(number-1)


def total():
    return 2**64 - 1
