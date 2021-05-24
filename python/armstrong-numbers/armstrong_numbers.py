def is_armstrong_number(number: int) -> bool:
    sum: int = 0
    run: int = number
    numbers = []
    while run != 0:
        numbers.append(run%10)
        run //= 10
    
    for n in numbers:
        sum += pow(n, len(numbers))
    
    print(sum)
    if sum == number:
        return True
    else:
        return False
    
