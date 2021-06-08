# my first thought was to use the sieve of eratosthenes
# but I figured that would be overkill for this exercise
# so I used a simple loop instead

def factors(value):
    number = value
    factors = []
    i = 2
    # We only need to look at numbers up to 
    # the square root of value.
    # This is a mathematical property that can be proved.
    while (i*i) <= value:
        if number % i == 0:
            # By repeatedly dividing out the factor, we ensure
            # that non-prime factors are not included in our results. 
            while number % i == 0:
                factors.append(i)
                number = number / i
        i += (i == 2)*1 + (i != 2)*2
    
    # If the remaining number is not 1,
    # it too must be a prime factor of value
    if number != 1:
        factors.append(number)

    return factors




