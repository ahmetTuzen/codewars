import math


def find_next_square(sq):
    i = int(math.sqrt(sq))
    return (i+1)**2 if i**2 == sq else -1
