from timeit import timeit


def isPalindrome_list(string):
    # Write your code here.
    lst = list(string)
    lst.reverse()
    return string == "".join(lst)


def isPalindrome_iter(string):
    # Write your code here.
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


def isPalindrome_slice(string):
    return string == string[::-1]


string = "asdfghjkjhgfdsa"
itr = 1_000_000

for foo in [isPalindrome_iter, isPalindrome_list, isPalindrome_slice]:
    t = timeit(stmt="foo(string)", number=itr, globals=globals())
    print(f"{foo.__name__} runed in {t:.6f} seconds")
