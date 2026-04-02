def is_valid_triangle(sides):
    a,b,c = sorted(sides)
    if a > 0 and (a+b >= c):
        return True
    return False

def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    a,b,c = sides
    return a==b==c

def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    a,b,c= sides
    return a==b or b==c or c==a

def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    return not isosceles(sides)

