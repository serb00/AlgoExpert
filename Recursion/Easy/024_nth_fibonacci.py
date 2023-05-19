from math import sqrt
from timeit import timeit


# O(1) time, O(1) space
def getNthFib_binet(n):
    '''
    Here we assume that #1 = 0. In Binet's formula #1 = 1.
    Therefore to use Binet's formula we forcing first case,
    else we're using Binet's formula with n = n - 1.
    '''
    # Write your code here.
    if n == 1:
        return 0
    else:
        num = n - 1
        float_result = (1/sqrt(5))*(((1+sqrt(5))/2)**num-((1-sqrt(5))/2**num))
        return round(float_result)


# O(n) time, O(1) space
def getNthFib_itr(n):
    # Write your code here.
    a, b = 0, 1
    counter = 3
    while counter <= n:
        a, b = b, a+b
        counter += 1
    return b if n > 1 else a


# O(n^2) time, O(n) space
def getNthFib_rec(n):
    # Write your code here.
    if n > 1:
        return getNthFib_rec(n-1) + getNthFib_rec(n-2)
    elif n == 0:
        return 1
    else:
        return 0


n = 20
itr = 10_000

for foo in [getNthFib_binet,
            getNthFib_itr,
            getNthFib_rec]:
    t = timeit(stmt="foo(n)", number=itr, globals=globals())
    print(f"{foo.__name__} {itr:,} runs took {t:.6f} seconds")
