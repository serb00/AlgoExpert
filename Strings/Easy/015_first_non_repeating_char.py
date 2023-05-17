from collections import Counter
from timeit import timeit


def firstNonRepeatingCharacter(string):
    # Write your code here.
    lst = Counter(string)
    for item in lst:
        if lst[item] == 1:
            return string.index(item)
    return -1


def firstNonRepeatingCharacter_dict(string):
    char_frequency = {}
    for char in string:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    for char in char_frequency:
        if char_frequency[char] == 1:
            return string.index(char)

    return -1


def firstNonRepeatingCharacter_count(string):
    for char in string:
        if string.count(char) == 1:
            return string.index(char)

    return -1


string = ("aaasdfghjkllkjhgfdsahjkasgdfjkhasgdfkjshagdfkjsahgdfkjhagk" +
          "fjhgsadkfjhgskdfjhgaskjdfhgaksjhdgfkasjhdgfkasjhgdfkjashgd" +
          "fkajshgdfkkjhsgdfkjhagsdfkjahsgdfkjgahskhjahsgdfssdvvssadz")

print(firstNonRepeatingCharacter(string))
itr = 100_000

for foo in [firstNonRepeatingCharacter,
            firstNonRepeatingCharacter_dict,
            firstNonRepeatingCharacter_count]:
    t = timeit(stmt="foo(string)", number=itr, globals=globals())
    print(f"{foo.__name__} {itr:,} runs took {t:.6f} seconds")
