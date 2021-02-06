def persistence(n):
    count = 0

    while n > 9:
        factor = 1
        for i in str(n):
            factor *= int(i)
        count += 1
        n = factor

    return count
