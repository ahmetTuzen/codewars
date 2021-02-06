def sum_pairs(ints, s):
    pair = []

    for i in ints:
        if s - i in pair:
            return [s-i, i]
        pair.append(i)
