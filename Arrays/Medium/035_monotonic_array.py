def isMonotonic(array):
    # Write your code here.
    p = 0
    increasing = None

    while p < len(array) - 1:
        if array[p] < array[p + 1]:
            if increasing is None:
                increasing = True
            elif increasing is False:
                return False
        elif array[p] > array[p + 1]:
            if increasing is None:
                increasing = False
            elif increasing is True:
                return False
        p += 1
    return True


array = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11]

print(isMonotonic(array))
