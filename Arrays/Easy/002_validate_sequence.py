from timeit import timeit


def isValidSubsequence(array, sequence):
    # Write your code here.
    current_element = 0
    for a in array:
        if a == sequence[current_element]:
            current_element += 1
        if current_element == len(sequence):
            return True
    return False


arr = [5, 1, 22, 25, 6, -1, 8, 10]
sq = [1, 6, -1, 10]
itr = 1_000_000

for foo in [isValidSubsequence]:
    t = timeit(stmt="foo(arr, sq)", number=itr, globals=globals())
    print(f"{foo.__name__} runed in {t:.6f} seconds")
