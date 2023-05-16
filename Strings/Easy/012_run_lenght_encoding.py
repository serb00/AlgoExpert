from timeit import timeit


def runLengthEncoding(string):
    # Write your code here.
    res = []
    fp = 0
    sp = 1
    ln = 1
    while sp <= len(string):
        if sp == len(string) or string[sp] != string[fp] or ln == 9:
            res.append(f'{ln}{string[fp]}')
            fp = sp
            sp += 1
            ln = 1
        else:
            sp += 1
            ln += 1
    return "".join(res)


def runLengthEncoding_list(string):
    # Write your code here.
    s_list = list(string)
    res = []
    fp = 0
    sp = 1
    ln = 1
    while sp <= len(s_list):
        if sp == len(s_list) or s_list[sp] != s_list[fp] or ln == 9:
            res.append(f'{ln}{s_list[fp]}')
            fp = sp
            sp += 1
            ln = 1
        else:
            sp += 1
            ln += 1
    return "".join(res)


# print(runLengthEncoding("AAAAAABBCCCDDDDDDDDRRRRADS"))
string = ("AAAAAABBCCCDDDDDDDDRRRRADSAAAAAABBCCCDDDDDDDDRRRRADSAAAA" +
          "AABBCCCDDDDDDDDRRRRADSAAAAAABBCCCDDDDDDDDRRRRADSAAAAAABB" +
          "CCCDDDDDDDDRRRRADSAAAAAABBCCCDDDDDDDDRRRRADSAAAAAABBCCCD" +
          "DDDDDDDRRRRADSAAAAAABBCCCDDDDDDDDRRRRADSAAAAAABBCCCDDDDD" +
          "DDDRRRRADSAAAAAABBCCCDDDDDDDDRRRRADSDDDDDDDRRRRADSDDDDDD")
itr = 10_000

for foo in [runLengthEncoding, runLengthEncoding_list]:
    t = timeit(stmt="foo(string)", number=itr, globals=globals())
    print(f"{foo.__name__} runed in {t:.6f} seconds")
