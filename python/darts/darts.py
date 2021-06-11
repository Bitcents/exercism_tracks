def calculate_distance(x, y) -> float:
    from math import sqrt
    return sqrt(x*x + y*y)

def score(x, y):
    dist_from_center = calculate_distance(x, y)
    return 10 - (dist_from_center > 1)*5 - (dist_from_center > 5)*4 - (dist_from_center > 10)*1
