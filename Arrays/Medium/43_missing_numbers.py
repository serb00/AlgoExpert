def missingNumbers(nums):
    # Write your code here.
    n = len(nums) + 2
    average = (sum(range(1, n+1))-sum(nums)) // 2
    sum1, sum2 = 0, 0

    for i in nums:
        if i <= average:
            sum1 += i
        else:
            sum2 += i

    sum1total = sum(range(1, average+1))
    sum2total = sum(range(average+1, n+1))

    return [sum1total - sum1, sum2total - sum2]


nums = [3]
print(missingNumbers(nums))
