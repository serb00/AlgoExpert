def twoNumberSum(array, targetSum):
    # Write your code here.
    res = []
    minus = [targetSum-a for a in array]
    for i in range(len(array)):
        if array[i] in minus[:i] or array[i] in minus[i+1:]:
            if array[i] not in res:
                res.append(array[i])
                res.append(minus[i])

    return res


def twoNumberSum2(array, targetSum):
    # Write your code here.
    st = set()
    for a in array:
        b = targetSum - a
        st.update({a})
        if b in st and b != a:
            return [a, b]
    return []


print(twoNumberSum2([3, 5, -4, 8, 11, 1, -1, 6], 10))
