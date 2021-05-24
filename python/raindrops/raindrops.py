def convert(number: int) -> str:
    string = ''
    not_divisible = True
    if number % 3 == 0:
        string += "Pling"
        not_divisible = False
    if number % 5 == 0:
        string += "Plang"
        not_divisible = False
    if number % 7 == 0:
        string += "Plong"
        not_divisible = False
    
    if not_divisible:
        return str(number)
    else:
        return string