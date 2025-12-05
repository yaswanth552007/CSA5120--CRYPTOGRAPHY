def create_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for c in key:
        if c not in used and c.isalpha():
            used.add(c)
            matrix.append(c)

    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in used:
            used.add(c)
            matrix.append(c)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_pos(matrix, letter):
    if letter == 'J':
        letter = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j


def playfair_encrypt(text, key):
    text = text.upper().replace("J", "I")
    matrix = create_matrix(key)

    # Prepare pairs
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            b = 'X'
            i += 1
        else:
            i += 2
        pairs.append((a, b))

    encrypted = ""
    for a, b in pairs:
        r1, c1 = find_pos(matrix, a)
        r2, c2 = find_pos(matrix, b)

        if r1 == r2:  
            encrypted += matrix[r1][(c1+1) % 5] + matrix[r2][(c2+1) % 5]
        elif c1 == c2:  
            encrypted += matrix[(r1+1) % 5][c1] + matrix[(r2+1) % 5][c2]
        else:
            encrypted += matrix[r1][c2] + matrix[r2][c1]

    return encrypted


# Example
print(playfair_encrypt("BALLOON", "MONARCHY"))
