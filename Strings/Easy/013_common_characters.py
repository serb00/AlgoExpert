from timeit import timeit


def commonCharacters(strings):
    # Write your code here.
    dic = dict()
    len_strings = len(strings)
    for s in strings:
        set_s = set(s)
        for char in set_s:
            dic[char] = dic[char] + 1 if char in dic.keys() else 1

    return [key for (key, value) in dic.items() if value == len_strings]


def commonCharacters_sets(strings):
    return list(set.intersection(*[{char for char in string}
                                   for string in strings]))


def commonCharacters_sets2(strings):
    return list(set.intersection(*[set(string) for string in strings]))


strings = ["abc", "bc", "c"]
# print(commonCharacters_sets(strings))
itr = 100_000

for foo in [commonCharacters, commonCharacters_sets, commonCharacters_sets2]:
    t = timeit(stmt="foo(strings)", number=itr, globals=globals())
    print(f"{foo.__name__} runed in {t:.6f} seconds")
