def is_valid_triangle(sides):
    side1,side2,side3 = sorted(sides)
    if side1 > 0 and (side1+side2 >= side3):
        return True
    return False

def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    side1,side2,side3 = sides
    return side1==side2==side3

def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    side1,side2,side3= sides
    return side1==side2 or side2==side3 or side3==side1

def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    return not isosceles(sides)
