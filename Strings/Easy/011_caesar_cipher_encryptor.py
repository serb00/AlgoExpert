from timeit import timeit


def caesarCipherEncryptor(string, key):
    # Write your code here.
    res = []
    key %= 26
    for char in string:
        newCode = (ord(char) + key - 97) % 26 + 97
        res.append(chr(newCode))
    return "".join(res)


def caesarCipherEncryptor_sol1(string, key):
    # Write your code here.
    res = []
    newKey = key % 26
    for char in string:
        res.append(getNewLetter1(char, newKey))
    return "".join(res)


def getNewLetter1(char, key):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    newLetterCode = alphabet.index(char) + key
    return alphabet[newLetterCode % 26]


def caesarCipherEncryptor_sol2(string, key):
    # Write your code here.
    res = []
    newKey = key % 26
    for char in string:
        res.append(getNewLetter2(char, newKey))
    return "".join(res)


def getNewLetter2(char, key):
    newLetterCode = ord(char) + key
    return (chr(newLetterCode) if newLetterCode <= 122 else
            chr(96 + newLetterCode % 122))


print(caesarCipherEncryptor("xyz", 2))


string = "asdfghjkjhgfdsaasdkjhasdlkjhmasd"
itr = 100_000

for foo in [caesarCipherEncryptor, caesarCipherEncryptor_sol1,
            caesarCipherEncryptor_sol2]:
    t = timeit(stmt="foo(string, 2)", number=itr, globals=globals())
    print(f"{foo.__name__} runed in {t:.6f} seconds")
