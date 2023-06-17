# O(n) time, O(1) space
# if we can mutate array and
# if numbers from 1 to n, where n - length of array
def firstDuplicateValue(array):
    # Write your code here.
    for A in array:
        cur = abs(A)
        if array[cur-1] < 0:
            return cur
        array[cur-1] = -array[cur-1]
    return -1


# O(n) time, O(n) space
def firstDuplicateValue_set(array):
    seen = set()
    for A in array:
        if A in seen:
            return A
        seen.add(A)

    return -1
