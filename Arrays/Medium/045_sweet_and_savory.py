def sweetAndSavory(dishes, target):
    # Write your code here.
    dishes.sort()
    best = float("inf")
    p1, p2 = 0, len(dishes) - 1
    bestpair = [0, 0]

    while p1 < p2:
        if dishes[p1] > 0 or dishes[p2] < 0:
            break
    
        curVal = (dishes[p2] + dishes[p1])
        if target - curVal < best and target >= curVal:
            best = target - curVal
            bestpair = [dishes[p1], dishes[p2]]
        if curVal < target and dishes[p1+1] < 0:
            p1 += 1
        else:
            p2 -= 1

    return bestpair


print(sweetAndSavory([-3, -5, 1, 7], 8))
