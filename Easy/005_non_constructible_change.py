from timeit import timeit


def nonConstructibleChange(coins):
    # Write your code here.
    change = 0
    if coins:
        coins.sort()
        for coin in coins:
            if coin > change + 1:
                change += 1
                return change
            change += coin
    return change + 1


# no sorting solution
# trouble is it's actually slower time wise than the first one
# but this solution could work with stream (when you do not
# know when you would stop getting numbers)
def nonConstructibleChange_opt(coins):
    # Write your code here.
    possible = 0b1
    for val in coins:
        # print('val = ', val)
        new = possible << val
        # print('new = ', new, ' ', bin(new))
        possible = possible | new
        # print('possible = ', possible, ' ', bin(possible))
    possible = bin(possible)
    # print(possible)

    cnt = 0
    for ch in range(len(possible) - 1, 1, -1):
        if possible[ch] == '0':
            break
        cnt += 1
    return cnt


print(nonConstructibleChange([5, 7, 2, 3, 1, 1, 22, 50]))


arr = [5, 7, 2, 3, 1, 1, 22, 50]
itr = 1_000_000

for foo in [nonConstructibleChange, nonConstructibleChange_opt]:
    t = timeit(stmt="foo(arr)", number=itr, globals=globals())
    print(f"{foo.__name__} runed in {t:.6f} seconds")
