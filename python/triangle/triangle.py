def equilateral(sides) -> bool:
    if sides == [0,0,0]:
        return False
    return (sides[0] == sides[1]) and (sides[1] == sides[2])


def isosceles(sides) -> bool:
    if sides == [0,0,0]:
        return False
    sides.sort()
    if not is_valid_triangle(sides):
        return False
    return (sides[0] == sides[1]) or (sides[1] == sides[2])


def scalene(sides) -> bool:
    if sides == [0,0,0]:
        return False
    sides.sort()
    if not is_valid_triangle(sides):
        return False
    return (not equilateral(sides)) and (not isosceles(sides))

def is_valid_triangle(sides) -> bool:
    return (sides[2] < sides[1] + sides[0])