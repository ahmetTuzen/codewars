def is_triangle(a, b, c):
    return a < b + c and a > b - c and a > c - b and a > 0 and b > 0 and c > 0
