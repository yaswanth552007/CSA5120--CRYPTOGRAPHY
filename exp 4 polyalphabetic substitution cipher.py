def poly_encrypt(text, key):
    text = text.upper()
    key = key.upper()
    res = ""
    j = 0

    for c in text:
        if c.isalpha():
            shift = ord(key[j % len(key)]) - 65
            res += chr((ord(c) - 65 + shift) % 26 + 65)
            j += 1
        else:
            res += c

    return res


# Example
print(poly_encrypt("YASWANTH", "KEY"))
