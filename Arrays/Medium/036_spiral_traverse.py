def spiralTraverse(array):
    # initiating corners
    sR, sC = 0, 0
    eR, eC = len(array) - 1, len(array[0]) - 1
    res = []

    while sR <= eR and sC <= eC:
        # move right in the upper row
        for col in range(sC, eC + 1):
            res.append(array[sR][col])

        # move down in the rightmost column,
        # ignoring row element we already added
        for row in range(sR + 1, eR + 1):
            res.append(array[row][eC])

        # move left in the lower row,
        # ignoring col element we already added
        for col in range(eC - 1, sC - 1, -1):
            # break in case of last row
            if sR == eR:
                break
            res.append(array[eR][col])

        # move up in the left most colum,
        # ignoring both top and bottom elements we already added
        for row in range(eR - 1, sR, -1):
            # break in case of last column
            if sC == eC:
                break
            res.append(array[row][sC])

        # changing corners
        sR += 1
        sC += 1
        eR -= 1
        eC -= 1

    return res


array = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ]

print(spiralTraverse(array))
