def binarySearch(array, target):
    # Write your code here.
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1
