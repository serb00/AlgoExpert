def mergeOverlappingIntervals(intervals):
    # Write your code here.
    # intervals.sort()
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    res = []
    res.append(intervals[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] <= res[-1][1] <= intervals[i][1]:
            res[-1][1] = intervals[i][1]
        elif intervals[i][0] > res[-1][1]:
            res.append(intervals[i])

    return res


intervals = [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
    ]
print(mergeOverlappingIntervals(intervals))
