def printer_error(s):
    return "{}/{}".format(len([char for char in s if char not in "abcdefghijklm"]), len(s))
