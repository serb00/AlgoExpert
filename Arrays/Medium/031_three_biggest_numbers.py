def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    res = []
    for idx in range(len(array)):
        left = idx + 1
        right = len(array) - 1
        while left < right:
            tempSum = array[idx] + array[left] + array[right]
            if tempSum == targetSum:
                res.append([array[idx], array[left], array[right]])
                left += 1
                right -= 1
            elif tempSum > targetSum:
                right -= 1
            else:
                left += 1
    return res


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
