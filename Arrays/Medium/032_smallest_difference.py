# O(n*m) time, where n, m = lenght of arrayOne and arrayTwo
# 0(1) space
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    dist = float("inf")
    res = []
    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            if abs(arrayOne[i] - arrayTwo[j]) < dist:
                dist = abs(arrayOne[i] - arrayTwo[j])
                res = [arrayOne[i], arrayTwo[j]]

    return res


# O(nlogn + mlogm) time, where n, m = lenght of arrayOne and arrayTwo
# 0(1) space
def smallestDifferenceOptimal(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    dist, res = float("inf"), []
    p1, p2 = 0, 0

    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        n1, n2 = arrayOne[p1], arrayTwo[p2]
        curDist = abs(n1 - n2)
        if curDist < dist:
            dist = curDist
            res = [n1, n2]
        if n1 > n2:
            p2 += 1
        else:
            p1 += 1

    return res
