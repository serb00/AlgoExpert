def selectionSort(array):
    # Write your code here.
    idx = 0
    while idx < len(array):
        min = idx
        for i in range(idx, len(array)):
            if array[i] < array[min]:
                min = i
        array[idx], array[min] = array[min], array[idx]
        idx += 1
    return array
