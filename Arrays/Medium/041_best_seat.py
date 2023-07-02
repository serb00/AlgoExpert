def bestSeat(seats):
    # Write your code here.
    beg, end, maxDist = 0, 0, 0
    seat = -1

    for i in range(1, len(seats)):
        if seats[i] == 0 and seats[i-1] == 1:
            beg = i
        if seats[i] == 1 and seats[i-1] == 0:
            end = i
            dist = end - beg
            if dist > maxDist:
                seat = (beg + end - 1) // 2
                maxDist = dist
    return seat


seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
print(bestSeat(seats))
