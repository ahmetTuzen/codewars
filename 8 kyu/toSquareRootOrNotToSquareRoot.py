def square_or_square_root(arr):
    return [i**.5 if (i**.5).is_integer() else i**2 for i in arr]
