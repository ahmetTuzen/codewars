def longest(s1, s2):
    return "".join(char for char in sorted(set([char for char in s1+s2])))
