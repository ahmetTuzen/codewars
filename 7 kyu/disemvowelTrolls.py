def disemvowel(string):
    return "".join("" if char in "aAeEiIoOuU" else char for char in string)
