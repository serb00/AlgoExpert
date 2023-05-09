def sortedSquaredArray(array):
    # Write your code here.
    res = [0] * len(array)
    a = 0
    b = len(array) - 1
    cur_element = b

    while a <= b:
        if abs(array[a]) > abs(array[b]):
            res[cur_element] = array[a] * array[a]
            a += 1
        else:
            res[cur_element] = array[b] * array[b]
            b -= 1
        cur_element -= 1

    return res


print(sortedSquaredArray([-10, -5, 0, 5, 10]))
