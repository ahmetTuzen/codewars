def to_alternating_case(string):
    return "".join(i.lower() if i.isupper() else i.upper() if i.islower() else i for i in string)
