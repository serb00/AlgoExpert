def insertionSort(array):
    # Write your code here.
    i = 1
    while i < len(array):
        for j in range(i - 1, -1, -1):
            if array[j+1] < array[j]:
                array[j+1], array[j] = array[j], array[j+1]
        i += 1
    return array


def insertionSort_opt(array):
    # Write your code here.
    i = 1
    while i < len(array):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
        i += 1
    return array


print(insertionSort([8, 5, 2, 9, 5, 6, 3]))
