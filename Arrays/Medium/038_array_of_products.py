def arrayOfProducts(array):
    # Write your code here.
    res = [1] * len(array)

    prod = 1
    for i in range(len(array)):
        res[i] = prod
        prod *= array[i]

    prod = 1
    for i in range(len(array) - 1, -1, -1):
        res[i] *= prod
        prod *= array[i]

    return res


array = [-5, 2, -4, 14, -6]
print(arrayOfProducts(array))
