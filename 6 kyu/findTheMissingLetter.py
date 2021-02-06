def find_missing_letter(chars):
    chars = [ord(char) for char in chars]
    for i in range(len(chars)-1):
        if chars[i+1] - chars[i] != 1:
            return chr(chars[i+1]-1)
