def xo(s):
    return sum(1 if char is "x" else -1 if char is "o" else 0 for char in s.lower()) == 0
