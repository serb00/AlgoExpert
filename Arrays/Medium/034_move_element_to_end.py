def moveElementToEnd(array, toMove):
    # Write your code here.
    p1, p2 = 0, len(array) - 1

    while p1 < p2:
        if array[p2] == toMove:
            p2 -= 1
        elif array[p1] == toMove:
            array[p1], array[p2] = array[p2], array[p1]
            p1 += 1
            p2 -= 1
        else:
            p1 += 1

    return array


array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

print(moveElementToEnd(array, toMove))
