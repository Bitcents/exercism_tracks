from math import sqrt

def triplets_with_sum(number):
    results = []
    for i in range(number//2, number//3, -1):
        for j in range(i-1,i//2,-1):
            k = sqrt(i*i - j*j)
            if i + j + k == number and k < j:
                results.append([int(k),j,i])
    return results

