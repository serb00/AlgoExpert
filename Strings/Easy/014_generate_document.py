from collections import Counter
from timeit import timeit


def generateDocument(characters, document):
    # Write your code here.
    hash = dict()
    for c in characters:
        hash[c] = hash[c] + 1 if c in hash else 1

    for c in document:
        if c not in hash or hash[c] == 0:
            return False
        hash[c] -= 1

    return True


def generateDocument_Counter(characters, document):
    return Counter(document) - Counter(characters) == {}


characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"

itr = 100_000

for foo in [generateDocument, generateDocument_Counter]:
    t = timeit(stmt="foo(characters, document)", number=itr, globals=globals())
    print(f"{foo.__name__} runed in {t:.6f} seconds")
