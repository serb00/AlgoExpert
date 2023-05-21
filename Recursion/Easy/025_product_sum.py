from timeit import timeit


def productSum(array, coeff=1):
    # Write your code here.
    sum = 0
    for i, v in enumerate(array):
        if type(v) is list:
            sum += productSum(v, coeff + 1)
        else:
            sum += v
    return sum * coeff


def productSum2(array, coeff=1):
    # Write your code here.
    sum = 0
    for v in array:
        if type(v) is list:
            sum += productSum(v, coeff + 1)
        else:
            sum += v
    return sum * coeff


n = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
itr = 1_000_000

for foo in [productSum,
            productSum2]:
    t = timeit(stmt="foo(n)", number=itr, globals=globals())
    print(f"{foo.__name__} {itr:,} runs took {t:.6f} seconds")
