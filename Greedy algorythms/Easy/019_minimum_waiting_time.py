# O(nlogn) time, O(n-1) space
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    res = [0]
    for i in range(1, len(queries)):
        res.append(res[i-1] + queries[i-1])

    return sum(res)


# O(nlogn) time, O(1) space
def minimumWaitingTime_opt(queries):
    # Write your code here.
    queries.sort()
    totalWaitingTime = 0
    for i in range(0, len(queries) - 1):
        queriesLeft = len(queries) - (i + 1)
        totalWaitingTime += queries[i] * queriesLeft

    return totalWaitingTime


def minimumWaitingTime_reversed(queries):
    # Write your code here.
    queries.sort(reverse=True)
    return sum(ind * value for ind, value in enumerate(queries))


queries = [3, 2, 1, 2, 6]

print(minimumWaitingTime(queries))
