def fake_bin(x):
    return "".join("0" if char in "01234" else "1" for char in x)
