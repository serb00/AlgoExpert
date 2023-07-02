def zeroSumSubarray(nums):
    # Write your code here.
    sums = set([0])
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum in sums:
            return True
        sums.add(currentSum)
    return False


nums = [1, 2, 3]
print(zeroSumSubarray(nums))
