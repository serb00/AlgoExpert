def findThreeLargestNumbers(array):
    # Write your code here.
    big1 = big2 = big3 = -float("inf")
    for i in range(len(array)):
        cur = array[i]
        if cur > big3:
            big1 = big2
            big2 = big3
            big3 = cur
        elif cur > big2:
            big1 = big2
            big2 = cur
        elif cur > big1:
            big1 = cur
    return [big1, big2, big3]
